import asyncio
import json
import time
import logging
import threading
import queue
from typing import Any, Dict
from matrice_common.stream.matrice_stream import MatriceStream
from matrice_inference.server.stream.utils import CameraConfig

class ProducerWorker:
    """Handles message production to streams."""
    
    def __init__(self, worker_id: int, output_queue: queue.PriorityQueue,
                 camera_configs: Dict[str, CameraConfig], message_timeout: float):
        self.worker_id = worker_id
        self.output_queue = output_queue
        self.camera_configs = camera_configs
        self.message_timeout = message_timeout
        self.running = False
        self.producer_streams = {}  # Will be created in worker thread's event loop
        self.logger = logging.getLogger(f"{__name__}.producer.{worker_id}")
    
    def start(self):
        """Start the producer worker in a separate thread."""
        self.running = True
        thread = threading.Thread(target=self._run, name=f"ProducerWorker-{self.worker_id}", daemon=False)
        thread.start()
        return thread
    
    def stop(self):
        """Stop the producer worker."""
        self.running = False
    
    def _run(self):
        """Main producer loop."""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        self.logger.info(f"Started producer worker {self.worker_id}")
        
        try:
            # Initialize streams for all cameras in this event loop
            loop.run_until_complete(self._initialize_streams())
            
            while self.running:
                try:
                    # Get task from output queue
                    try:
                        priority, timestamp, task_data = self.output_queue.get(timeout=self.message_timeout)
                    except queue.Empty:
                        continue
                    
                    # Send message to stream
                    loop.run_until_complete(self._send_message_safely(task_data))
                    
                except Exception as e:
                    self.logger.error(f"Producer error: {e}")
                    time.sleep(0.1)
        
        finally:
            # Clean up streams
            for stream in self.producer_streams.values():
                try:
                    loop.run_until_complete(stream.async_close())
                except Exception as e:
                    self.logger.error(f"Error closing producer stream: {e}")
            loop.close()
            self.logger.info(f"Producer worker {self.worker_id} stopped")

    async def _initialize_streams(self):
        """Initialize producer streams for all cameras in the current event loop."""
        try:
            from matrice_common.stream.matrice_stream import MatriceStream, StreamType
            
            for camera_id, camera_config in self.camera_configs.items():
                try:
                    stream_config = camera_config.stream_config
                    output_topic = camera_config.output_topic
                    
                    # Determine stream type
                    stream_type = StreamType.KAFKA if stream_config.get("stream_type", "kafka").lower() == "kafka" else StreamType.REDIS
                    
                    # Create stream configuration
                    if stream_type == StreamType.KAFKA:
                        stream_params = {
                            "bootstrap_servers": stream_config.get("bootstrap_servers", "localhost:9092"),
                            "sasl_username": stream_config.get("sasl_username", "matrice-sdk-user"),
                            "sasl_password": stream_config.get("sasl_password", "matrice-sdk-password"),
                            "sasl_mechanism": stream_config.get("sasl_mechanism", "SCRAM-SHA-256"),
                            "security_protocol": stream_config.get("security_protocol", "SASL_PLAINTEXT"),
                        }
                    else:  # Redis
                        stream_params = {
                            "host": stream_config.get("host", "localhost"),
                            "port": stream_config.get("port", 6379),
                            "password": stream_config.get("password"),
                            "username": stream_config.get("username"),
                            "db": stream_config.get("db", 0),
                        }
                    
                    # Create and setup producer stream
                    producer_stream = MatriceStream(stream_type, **stream_params)
                    await producer_stream.async_setup(output_topic)
                    self.producer_streams[camera_id] = producer_stream
                    
                    self.logger.info(f"Initialized {stream_type.value} producer stream for camera {camera_id} in worker {self.worker_id}")
                    
                except Exception as e:
                    self.logger.error(f"Failed to initialize producer stream for camera {camera_id}: {e}")
                    continue
                    
        except Exception as e:
            self.logger.error(f"Failed to initialize producer streams: {e}")
            raise
    
    async def _send_message_safely(self, task_data: Dict[str, Any]):
        """Send message to the appropriate stream safely."""
        try:
            camera_id = task_data["camera_id"]
            message_key = task_data["message_key"]
            data = task_data["data"]
            
            # Check if camera and stream still exist
            if camera_id not in self.producer_streams or camera_id not in self.camera_configs:
                self.logger.warning(f"Camera {camera_id} not found in producer streams or configs")
                return
            
            camera_config = self.camera_configs[camera_id]
            if not camera_config.enabled:
                self.logger.debug(f"Camera {camera_id} is disabled, skipping message")
                return
            
            # Get producer stream for camera
            producer_stream = self.producer_streams[camera_id]
            output_topic = camera_config.output_topic
            
            # Send message to stream
            await producer_stream.async_add_message(
                output_topic,
                json.dumps(data),
                key=message_key
            )
            
        except Exception as e:
            self.logger.error(f"Error sending message: {e}")

