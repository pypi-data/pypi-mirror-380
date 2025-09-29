import asyncio
import json
import time
import logging
import threading
import queue
from typing import Any, Dict
from concurrent.futures import ThreadPoolExecutor

class InferenceWorker:
    """Handles inference processing using threading."""
    
    def __init__(self, worker_id: int, inference_queue: queue.PriorityQueue,
                 postproc_queue: queue.PriorityQueue, inference_executor: ThreadPoolExecutor,
                 message_timeout: float, inference_timeout: float, inference_interface=None):
        self.worker_id = worker_id
        self.inference_queue = inference_queue
        self.postproc_queue = postproc_queue
        self.inference_executor = inference_executor
        self.message_timeout = message_timeout
        self.inference_timeout = inference_timeout
        self.inference_interface = inference_interface
        self.running = False
        self.logger = logging.getLogger(f"{__name__}.inference.{worker_id}")
    
    def start(self):
        """Start the inference worker in a separate thread."""
        self.running = True
        thread = threading.Thread(target=self._run, name=f"InferenceWorker-{self.worker_id}", daemon=False)
        thread.start()
        return thread
    
    def stop(self):
        """Stop the inference worker."""
        self.running = False
    
    def _run(self):
        """Main inference dispatcher loop."""
        self.logger.info(f"Started inference worker {self.worker_id}")
        
        while self.running:
            try:
                # Get task from inference queue
                try:
                    priority, timestamp, task_data = self.inference_queue.get(timeout=self.message_timeout)
                except queue.Empty:
                    continue
                
                # Process inference task
                self._process_inference_task(priority, task_data)
                
            except Exception as e:
                self.logger.error(f"Inference worker error: {e}")
        
        self.logger.info(f"Inference worker {self.worker_id} stopped")
    
    def _process_inference_task(self, priority: int, task_data: Dict[str, Any]):
        """Process a single inference task."""
        try:
            message = task_data["message"]
            
            # Submit to thread pool for async execution
            start_time = time.time()
            future = self.inference_executor.submit(self._run_inference, task_data)
            result = future.result(timeout=self.inference_timeout)
            processing_time = time.time() - start_time
            
            if result["success"]:
                # Create post-processing task
                postproc_task = {
                    "original_message": message,
                    "model_result": result["model_result"],
                    "metadata": result["metadata"],
                    "processing_time": processing_time,
                    "input_stream": task_data["input_stream"],
                    "stream_key": task_data["stream_key"],
                    "camera_config": task_data["camera_config"]
                }
                
                # Add to post-processing queue with timestamp as tie-breaker
                self.postproc_queue.put((priority, time.time(), postproc_task))
            else:
                self.logger.error(f"Inference failed: {result['error']}")
                
        except Exception as e:
            self.logger.error(f"Inference task error: {e}")

    def _run_inference(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Run inference in thread pool."""
        try:
            # Extract task data - handle camera streamer format
            input_stream_data = task_data.get("input_stream", {})
            input_content = input_stream_data.get("content")
            
            # Handle base64 encoded content from camera streamer
            if input_content and isinstance(input_content, str):
                import base64
                try:
                    input_content = base64.b64decode(input_content)
                except Exception as e:
                    logging.warning(f"Failed to decode base64 input: {str(e)}")
            
            stream_key = task_data.get("stream_key")
            stream_info = input_stream_data.get("stream_info", {})
            camera_info = input_stream_data.get("camera_info", {})
            extra_params = task_data.get("extra_params", {})
            
            # Ensure extra_params is a dictionary
            if not isinstance(extra_params, dict):
                logging.warning(f"extra_params is not a dict in inference worker, converting from {type(extra_params)}: {extra_params}")
                if isinstance(extra_params, list):
                    # Convert list to dict if possible
                    if len(extra_params) == 0:
                        extra_params = {}
                    elif all(isinstance(item, dict) for item in extra_params):
                        # Merge all dictionaries in the list
                        merged_params = {}
                        for item in extra_params:
                            merged_params.update(item)
                        extra_params = merged_params
                    else:
                        extra_params = {}
                else:
                    extra_params = {}
            
            if self.inference_interface is None:
                raise ValueError("Inference interface not initialized")
            
            # Create event loop for this thread if it doesn't exist
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            # Perform inference
            model_result, metadata = loop.run_until_complete(
                self.inference_interface.inference(
                    input=input_content,
                    extra_params=extra_params,
                    apply_post_processing=False,  # Inference only
                    stream_key=stream_key,
                    stream_info=stream_info,
                    camera_info=camera_info
                )
            )
            
            return {
                "model_result": model_result,
                "metadata": metadata,
                "success": True,
                "error": None
            }
            
        except Exception as e:
            logging.error(f"Inference worker error: {str(e)}", exc_info=True)
            return {
                "model_result": None,
                "metadata": None,
                "success": False,
                "error": str(e)
            }

