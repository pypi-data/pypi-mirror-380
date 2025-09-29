"""
Ultra-optimized streaming pipeline using MatriceStream and updated inference interface:
Direct processing with priority queues, dynamic camera configuration

Architecture:
Consumer workers (threading) -> Priority Queue -> Inference workers (threading) -> 
Priority Queue -> Post-processing workers (threading) -> Priority Queue -> Producer workers (threading)

Features:
- Start without initial configuration
- Dynamic camera configuration while running
- Support for both Kafka and Redis streams
- Integration with updated InferenceInterface and PostProcessor
- Maximum throughput with direct processing
- Low latency with no batching delays  
- Multi-camera support with topic routing
- Thread-based parallelism for inference and post-processing
- Non-blocking threading for consumers/producers
"""

import asyncio
import json
import time
import logging
import threading
import queue
import signal
import copy
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List, Union
from concurrent.futures import ThreadPoolExecutor

from matrice_common.stream.matrice_stream import MatriceStream, StreamType
from matrice_analytics.post_processing.post_processor import PostProcessor

from matrice_inference.server.inference_interface import InferenceInterface
from matrice_inference.server.model.model_manager_wrapper import ModelManagerWrapper
from matrice_inference.server.stream.utils import CameraConfig, StreamMessage
from matrice_inference.server.stream.consumer_worker import ConsumerWorker
from matrice_inference.server.stream.inference_worker import InferenceWorker
from matrice_inference.server.stream.post_processing_worker import PostProcessingWorker
from matrice_inference.server.stream.producer_worker import ProducerWorker
# from matrice_inference.server.stream.frame_cache import RedisFrameCache



class StreamingPipeline:
    """Ultra-optimized streaming pipeline with dynamic camera configuration."""
    
    def __init__(
        self,
        inference_interface: InferenceInterface,
        post_processor: PostProcessor,
        consumer_threads=1,
        producer_threads=1,
        inference_threads=1,
        postprocessing_threads=1,
        inference_queue_maxsize=5000,
        postproc_queue_maxsize=5000,
        output_queue_maxsize=5000,
        message_timeout=10.0,
        inference_timeout=30.0,
        shutdown_timeout=30.0,
        camera_configs: Optional[Dict[str, CameraConfig]] = None,
    ):
        self.inference_interface = inference_interface
        self.post_processor = post_processor
        self.consumer_threads = consumer_threads
        self.producer_threads = producer_threads
        self.inference_threads = inference_threads
        self.postprocessing_threads = postprocessing_threads
        self.inference_queue_maxsize = inference_queue_maxsize
        self.postproc_queue_maxsize = postproc_queue_maxsize
        self.output_queue_maxsize = output_queue_maxsize
        self.message_timeout = message_timeout
        self.inference_timeout = inference_timeout
        self.shutdown_timeout = shutdown_timeout
        
        # Camera configurations (can be empty initially)
        self.camera_configs: Dict[str, CameraConfig] = camera_configs or {}
        
        # Priority queues for pipeline stages
        self.inference_queue = queue.PriorityQueue(maxsize=self.inference_queue_maxsize)
        self.postproc_queue = queue.PriorityQueue(maxsize=self.postproc_queue_maxsize)
        self.output_queue = queue.PriorityQueue(maxsize=self.output_queue_maxsize)
        
        # Thread pools for CPU/GPU intensive work
        self.inference_executor = ThreadPoolExecutor(self.inference_threads)
        self.postprocessing_executor = ThreadPoolExecutor(self.postprocessing_threads)
        
        # No centralized stream management - each worker creates its own streams
        
        # Worker instances
        self.consumer_workers: Dict[str, List[ConsumerWorker]] = {}
        self.inference_workers = []
        self.postproc_workers = []
        self.producer_workers = []
        
        # Worker threads
        self.worker_threads = []
        
        # Control state
        self.running = False
        
        self.logger = logging.getLogger(__name__)
        
        # Frame cache disabled (commented out)
        # self.frame_cache_config = frame_cache_config or {}
        # self.frame_cache: Optional[RedisFrameCache] = None
    
    # Removed set_global_instances method - now passing interfaces as parameters to worker functions
    
    async def start(self):
        """Start the pipeline."""
        if self.running:
            self.logger.warning("Pipeline already running")
            return
        
        self.running = True
        self.logger.info("Starting ultra-optimized streaming pipeline...")
        
        try:
            # Frame cache initialization disabled
            # fc = dict(self.frame_cache_config)
            # if not fc.get("host"):
            #     for cfg in self.camera_configs.values():
            #         sc = cfg.stream_config
            #         if sc.get("stream_type", "kafka").lower() == "redis":
            #             fc.setdefault("host", sc.get("host", "localhost"))
            #             fc.setdefault("port", sc.get("port", 6379))
            #             fc.setdefault("password", sc.get("password"))
            #             fc.setdefault("username", sc.get("username"))
            #             fc.setdefault("db", sc.get("db", 0))
            #             break
            # try:
            #     self.frame_cache = RedisFrameCache(
            #         host=fc.get("host", "localhost"),
            #         port=fc.get("port", 6379),
            #         db=fc.get("db", 0),
            #         password=fc.get("password"),
            #         username=fc.get("username"),
            #         ttl_seconds=fc.get("ttl_seconds", 300),
            #         prefix=fc.get("prefix", "stream:frames:"),
            #     )
            #     self.frame_cache.start()
            # except Exception as _:
            #     self.frame_cache = None
            #     self.logger.warning("Frame cache initialization failed; proceeding without cache")
            
            # Initialize streams for existing camera configs
            await self._initialize_streams()
            
            # Create and start workers
            await self._create_workers()
            self._start_workers()
            
            self.logger.info(
                f"Pipeline started with {len(self.camera_configs)} cameras, "
                f"{sum(len(workers) for workers in self.consumer_workers.values())} consumer workers, "
                f"{len(self.inference_workers)} inference workers, "
                f"{len(self.postproc_workers)} post-processing workers, "
                f"{len(self.producer_workers)} producer workers"
            )
            
        except Exception as e:
            self.logger.error(f"Failed to start pipeline: {e}")
            await self.stop()
            raise
    
    async def stop(self):
        """Stop the pipeline gracefully."""
        if not self.running:
            return
        
        self.logger.info("Stopping pipeline...")
        self.running = False
        
        # Stop all workers
        self._stop_workers()
        
        # Wait for all threads to complete
        for thread in self.worker_threads:
            if thread.is_alive():
                thread.join(timeout=self.shutdown_timeout)
        
        # Close streams
        await self._close_streams()
        
        # Shutdown executors
        self.inference_executor.shutdown(wait=False)
        self.postprocessing_executor.shutdown(wait=False)
        
        # Frame cache stop disabled
        # try:
        #     if self.frame_cache:
        #         self.frame_cache.stop()
        # except Exception:
        #     pass
        
        self.logger.info("Pipeline stopped")
    
    async def add_camera_config(self, camera_config: CameraConfig) -> bool:
        """
        Add a camera configuration dynamically while pipeline is running.
        
        Args:
            camera_config: Camera configuration to add
            
        Returns:
            bool: True if successfully added, False otherwise
        """
        try:
            camera_id = camera_config.camera_id
            
            if camera_id in self.camera_configs:
                self.logger.warning(f"Camera {camera_id} already exists, updating configuration")
                # Stop existing workers for this camera
                await self._stop_camera_workers(camera_id)
            
            # Add camera config
            self.camera_configs[camera_id] = camera_config
            
            # Create workers for this camera if pipeline is running
            if self.running:
                await self._create_camera_workers(camera_config)
                self._start_camera_workers(camera_id)
            
            self.logger.info(f"Successfully added camera configuration for {camera_id}")
            return True
                
        except Exception as e:
            self.logger.error(f"Failed to add camera config for {camera_config.camera_id}: {str(e)}")
            return False
    
    async def remove_camera_config(self, camera_id: str) -> bool:
        """
        Remove a camera configuration dynamically.
        
        Args:
            camera_id: ID of camera to remove
            
        Returns:
            bool: True if successfully removed, False otherwise
        """
        try:
            if camera_id not in self.camera_configs:
                self.logger.warning(f"Camera {camera_id} does not exist")
                return False
            
            # Stop workers for this camera
            await self._stop_camera_workers(camera_id)
            
            # Remove camera config
            del self.camera_configs[camera_id]
            
            self.logger.info(f"Successfully removed camera configuration for {camera_id}")
            return True
                
        except Exception as e:
            self.logger.error(f"Failed to remove camera config for {camera_id}: {str(e)}")
            return False
    
    async def update_camera_config(self, camera_config: CameraConfig) -> bool:
        """
        Update an existing camera configuration.
        
        Args:
            camera_config: Updated camera configuration
            
        Returns:
            bool: True if successfully updated, False otherwise
        """
        return await self.add_camera_config(camera_config)
    
    def enable_camera(self, camera_id: str) -> bool:
        """Enable a camera."""
        if camera_id in self.camera_configs:
            self.camera_configs[camera_id].enabled = True
            self.logger.info(f"Camera {camera_id} enabled")
            return True
        return False
    
    def disable_camera(self, camera_id: str) -> bool:
        """Disable a camera."""
        if camera_id in self.camera_configs:
            self.camera_configs[camera_id].enabled = False
            self.logger.info(f"Camera {camera_id} disabled")
            return True
        return False
    
    async def _initialize_streams(self):
        """No centralized stream initialization - workers create their own streams."""
        pass
    
    async def _initialize_camera_streams(self, camera_config: CameraConfig):
        """No centralized camera stream initialization - workers create their own streams."""
        pass
    
    async def _close_streams(self):
        """No centralized streams to close - workers manage their own streams."""
        pass
    
    async def _close_camera_streams(self, camera_id: str):
        """No centralized camera streams to close - workers manage their own streams."""
        pass
    
    async def _create_workers(self):
        """Create all worker instances."""
        # Create consumer workers (per camera)
        for camera_config in self.camera_configs.values():
            await self._create_camera_workers(camera_config)
        
        # Create inference workers
        for i in range(self.inference_threads):
            worker = InferenceWorker(
                worker_id=i,
                inference_queue=self.inference_queue,
                postproc_queue=self.postproc_queue,
                inference_executor=self.inference_executor,
                message_timeout=self.message_timeout,
                inference_timeout=self.inference_timeout,
                inference_interface=self.inference_interface
            )
            self.inference_workers.append(worker)
        
        # Create post-processing workers
        for i in range(self.postprocessing_threads):
            worker = PostProcessingWorker(
                worker_id=i,
                postproc_queue=self.postproc_queue,
                output_queue=self.output_queue,
                postprocessing_executor=self.postprocessing_executor,
                message_timeout=self.message_timeout,
                inference_timeout=self.inference_timeout,
                post_processor=self.post_processor,
                # frame_cache=self.frame_cache,
            )
            self.postproc_workers.append(worker)
        
        # Create producer workers
        for i in range(self.producer_threads):
            worker = ProducerWorker(
                worker_id=i,
                output_queue=self.output_queue,
                camera_configs=self.camera_configs,
                message_timeout=self.message_timeout
            )
            self.producer_workers.append(worker)
    
    async def _create_camera_workers(self, camera_config: CameraConfig):
        """Create consumer workers for a specific camera."""
        camera_id = camera_config.camera_id
        
        # Create consumer workers for this camera - each worker will create its own stream
        camera_workers = []
        for i in range(self.consumer_threads):
            worker = ConsumerWorker(
                camera_id=camera_id,
                worker_id=i,
                stream_config=camera_config.stream_config,
                input_topic=camera_config.input_topic,
                inference_queue=self.inference_queue,
                message_timeout=self.message_timeout,
                camera_config=camera_config
            )
            camera_workers.append(worker)
        
        self.consumer_workers[camera_id] = camera_workers
    
    def _start_workers(self):
        """Start all worker instances."""
        # Start consumer workers
        for camera_id in self.consumer_workers:
            self._start_camera_workers(camera_id)
        
        # Start inference workers
        for worker in self.inference_workers:
            thread = worker.start()
            self.worker_threads.append(thread)
        
        # Start post-processing workers
        for worker in self.postproc_workers:
            thread = worker.start()
            self.worker_threads.append(thread)
        
        # Start producer workers
        for worker in self.producer_workers:
            thread = worker.start()
            self.worker_threads.append(thread)
    
    def _start_camera_workers(self, camera_id: str):
        """Start consumer workers for a specific camera."""
        if camera_id in self.consumer_workers:
            for worker in self.consumer_workers[camera_id]:
                thread = worker.start()
                self.worker_threads.append(thread)
    
    def _stop_workers(self):
        """Stop all worker instances."""
        # Stop all workers
        for workers in self.consumer_workers.values():
            for worker in workers:
                worker.stop()
        
        for worker in (self.inference_workers + self.postproc_workers + self.producer_workers):
            worker.stop()
    
    async def _stop_camera_workers(self, camera_id: str):
        """Stop consumer workers for a specific camera."""
        if camera_id in self.consumer_workers:
            for worker in self.consumer_workers[camera_id]:
                worker.stop()
            # Remove from tracking
            del self.consumer_workers[camera_id]
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get pipeline metrics."""
        return {
            "running": self.running,
            "camera_count": len(self.camera_configs),
            "enabled_cameras": sum(1 for config in self.camera_configs.values() if config.enabled),
            "queue_sizes": {
                "inference": self.inference_queue.qsize(),
                "postproc": self.postproc_queue.qsize(),
                "output": self.output_queue.qsize(),
            },
            "worker_counts": {
                "consumers": sum(len(workers) for workers in self.consumer_workers.values()),
                "inference_workers": len(self.inference_workers),
                "postproc_workers": len(self.postproc_workers),
                "producers": len(self.producer_workers),
            },
            "thread_counts": {
                "total_threads": len(self.worker_threads),
                "active_threads": len([t for t in self.worker_threads if t.is_alive()]),
            },
            "thread_pool_sizes": {
                "inference_threads": self.inference_threads,
                "postprocessing_threads": self.postprocessing_threads,
            },
            "camera_configs": {
                camera_id: {
                    "input_topic": config.input_topic,
                    "output_topic": config.output_topic,
                    "enabled": config.enabled,
                    "stream_type": config.stream_config.get("stream_type", "kafka")
                }
                for camera_id, config in self.camera_configs.items()
            }
        }

