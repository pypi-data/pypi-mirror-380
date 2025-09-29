import asyncio
import logging
import threading
import queue
import time
from typing import Any, Dict
from concurrent.futures import ThreadPoolExecutor


class PostProcessingWorker:
    """Handles post-processing using threading."""
    
    def __init__(self, worker_id: int, postproc_queue: queue.PriorityQueue,
                 output_queue: queue.PriorityQueue, postprocessing_executor: ThreadPoolExecutor,
                 message_timeout: float, inference_timeout: float, post_processor=None,
                 frame_cache=None):
        self.worker_id = worker_id
        self.postproc_queue = postproc_queue
        self.output_queue = output_queue
        self.postprocessing_executor = postprocessing_executor
        self.message_timeout = message_timeout
        self.inference_timeout = inference_timeout
        self.post_processor = post_processor
        self.frame_cache = frame_cache
        self.running = False
        self.logger = logging.getLogger(f"{__name__}.postproc.{worker_id}")
    
    def start(self):
        """Start the post-processing worker in a separate thread."""
        self.running = True
        thread = threading.Thread(target=self._run, name=f"PostProcWorker-{self.worker_id}", daemon=False)
        thread.start()
        return thread
    
    def stop(self):
        """Stop the post-processing worker."""
        self.running = False
    
    def _run(self):
        """Main post-processing dispatcher loop."""
        self.logger.info(f"Started post-processing worker {self.worker_id}")
        
        while self.running:
            try:
                # Get task from post-processing queue
                try:
                    priority, timestamp, task_data = self.postproc_queue.get(timeout=self.message_timeout)
                except queue.Empty:
                    continue
                
                # Process post-processing task
                self._process_postproc_task(priority, task_data)
                
            except Exception as e:
                self.logger.error(f"Post-processing worker error: {e}")
        
        self.logger.info(f"Post-processing worker {self.worker_id} stopped")
    
    def _process_postproc_task(self, priority: int, task_data: Dict[str, Any]):
        """Process a single post-processing task."""
        try:
            # Submit to thread pool for async execution
            future = self.postprocessing_executor.submit(self._run_post_processing, task_data)
            result = future.result(timeout=self.inference_timeout)
            
            if result["success"]:
                # Cache disabled: preserving content in output and not pushing to Redis
                # try:
                #     orig_input = task_data.get("input_stream", {}) or {}
                #     content = orig_input.get("content")
                #     frame_id_for_cache = task_data.get("frame_id") or orig_input.get("frame_id")
                #     if content and frame_id_for_cache and self.frame_cache:
                #         if isinstance(content, bytes):
                #             import base64
                #             try:
                #                 content = base64.b64encode(content).decode("ascii")
                #             except Exception:
                #                 content = None
                #         if isinstance(content, str):
                #             self.frame_cache.put(frame_id_for_cache, content)
                # except Exception:
                #     pass

                # Create final output message
                # Prepare input_stream for output: ensure frame_id is present and strip bulky content
                safe_input_stream = {}
                try:
                    if isinstance(task_data.get("input_stream"), dict):
                        safe_input_stream = dict(task_data["input_stream"])  # shallow copy
                        # Ensure frame_id propagation
                        if "frame_id" not in safe_input_stream and "frame_id" in task_data:
                            safe_input_stream["frame_id"] = task_data["frame_id"]
                        # Do not strip content; keep as-is in output
                        # if "content" in safe_input_stream:
                        #     safe_input_stream["content"] = ""
                except Exception:
                    safe_input_stream = task_data.get("input_stream", {})

                # Determine frame_id for top-level convenience
                frame_id = task_data.get("frame_id")
                if not frame_id and isinstance(safe_input_stream, dict):
                    frame_id = safe_input_stream.get("frame_id")

                output_data = {
                    "camera_id": task_data["original_message"].camera_id,
                    "message_key": task_data["original_message"].message_key,
                    "timestamp": task_data["original_message"].timestamp.isoformat(),
                    "frame_id": frame_id,
                    "model_result": task_data["model_result"],
                    "input_stream": safe_input_stream,
                    "post_processing_result": result["post_processing_result"],
                    "processing_time_sec": task_data["processing_time"],
                    "metadata": task_data.get("metadata", {})
                }
                
                # Add to output queue
                output_task = {
                    "camera_id": task_data["original_message"].camera_id,
                    "message_key": task_data["original_message"].message_key,
                    "data": output_data,
                }
                # Add to output queue with timestamp as tie-breaker
                self.output_queue.put((priority, time.time(), output_task))
            else:
                self.logger.error(f"Post-processing failed: {result['error']}")
                
        except Exception as e:
            self.logger.error(f"Post-processing task error: {e}")

    def _run_post_processing(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Run post-processing in thread pool."""
        try:
            if self.post_processor is None:
                raise ValueError("Post processor not initialized")
            
            # Extract task data
            model_result = task_data["model_result"]
            input_stream_data = task_data.get("input_stream", {})
            input_content = input_stream_data.get("content")
            
            # Handle base64 encoded content
            if input_content and isinstance(input_content, str):
                import base64
                try:
                    input_content = base64.b64decode(input_content)
                except Exception as e:
                    logging.warning(f"Failed to decode base64 input: {str(e)}")
                    input_content = None
            
            stream_key = task_data.get("stream_key")
            stream_info = input_stream_data.get("stream_info", {})
            camera_config = task_data.get("camera_config", {})
            
            # Create event loop for this thread if it doesn't exist
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            # Perform post-processing
            result = loop.run_until_complete(
                self.post_processor.process(
                    data=model_result,
                    input_bytes=input_content if isinstance(input_content, bytes) else None,
                    stream_key=stream_key,
                    stream_info=stream_info
                )
            )
            
            # For face recognition use case, return empty raw results
            processed_raw_results = []
            try:
                if hasattr(result, 'usecase') and not result.usecase == 'face_recognition':
                    processed_raw_results = model_result
            except Exception as e:
                logging.warning(f"Failed to get processed raw results: {str(e)}")
            
            # Extract agg_summary from result data if available
            agg_summary = {}
            try:
                if hasattr(result, 'data') and isinstance(result.data, dict):
                    agg_summary = result.data.get("agg_summary", {})
            except Exception as e:
                logging.warning(f"Failed to get agg summary: {str(e)}")

            # Format result similar to InferenceInterface
            if result.is_success():
                post_processing_result = {
                    "status": "success",
                    "processing_time": result.processing_time,
                    "usecase": getattr(result, 'usecase', ''),
                    "category": getattr(result, 'category', ''),
                    "summary": getattr(result, 'summary', ''),
                    "insights": getattr(result, 'insights', []),
                    "metrics": getattr(result, 'metrics', {}),
                    "predictions": getattr(result, 'predictions', []),
                    "agg_summary": agg_summary,
                    "raw_results": processed_raw_results,
                    "stream_key": stream_key
                }
            else:
                post_processing_result = {
                    "status": "post_processing_failed",
                    "error": result.error_message,
                    "error_type": getattr(result, 'error_type', 'ProcessingError'),
                    "processing_time": result.processing_time,
                    "stream_key": stream_key,
                    "agg_summary": agg_summary,
                    "raw_results": model_result
                }
            
            return {
                "post_processing_result": post_processing_result,
                "success": True,
                "error": None
            }
            
        except Exception as e:
            logging.error(f"Post-processing worker error: {str(e)}", exc_info=True)
            return {
                "post_processing_result": {
                    "status": "post_processing_failed",
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "stream_key": task_data.get("stream_key")
                },
                "success": False,
                "error": str(e)
            }
