# Import moved to method where it's needed to avoid circular imports
from matrice_inference.server.stream.utils import CameraConfig, StreamMessage
import asyncio
import json
import time
import logging
import threading
import queue
from datetime import datetime, timezone
import logging

class ConsumerWorker:
    """Handles message consumption from streams."""
    
    def __init__(self, camera_id: str, worker_id: int, stream_config: dict, input_topic: str,
                 inference_queue: queue.PriorityQueue, message_timeout: float,
                 camera_config: CameraConfig):
        self.camera_id = camera_id
        self.worker_id = worker_id
        self.stream_config = stream_config
        self.input_topic = input_topic
        self.inference_queue = inference_queue
        self.message_timeout = message_timeout
        self.camera_config = camera_config
        self.running = False
        self.stream = None  # Will be created in worker thread's event loop
        self.logger = logging.getLogger(f"{__name__}.consumer.{camera_id}.{worker_id}")
    
    def start(self):
        """Start the consumer worker in a separate thread."""
        self.running = True
        thread = threading.Thread(target=self._run, name=f"Consumer-{self.camera_id}-{self.worker_id}", daemon=False)
        thread.start()
        return thread
    
    def stop(self):
        """Stop the consumer worker."""
        self.running = False
    
    def _run(self):
        """Main consumer loop."""
        # Create a new event loop for this worker thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        self.logger.info(f"Started consumer worker for camera {self.camera_id}")
        
        try:
            # Initialize stream in this event loop
            loop.run_until_complete(self._initialize_stream())
            
            while self.running and self.camera_config.enabled:
                try:
                    # Get message from stream
                    message_data = loop.run_until_complete(
                        self._get_message_safely()
                    )
                    
                    if not message_data:
                        continue
                    
                    # Parse and create task
                    self._process_message(message_data)
                        
                except Exception as e:
                    self.logger.error(f"Consumer error: {e}")
                    time.sleep(1.0)
        
        finally:
            # Clean up stream
            if self.stream:
                try:
                    loop.run_until_complete(self.stream.async_close())
                except Exception as e:
                    self.logger.error(f"Error closing stream: {e}")
            loop.close()
            self.logger.info(f"Consumer worker stopped for camera {self.camera_id}")

    async def _initialize_stream(self):
        """Initialize MatriceStream in the current event loop."""
        try:
            from matrice_common.stream.matrice_stream import MatriceStream, StreamType
            
            # Determine stream type
            stream_type = StreamType.KAFKA if self.stream_config.get("stream_type", "kafka").lower() == "kafka" else StreamType.REDIS
            
            # Create stream configuration
            if stream_type == StreamType.KAFKA:
                stream_params = {
                    "bootstrap_servers": self.stream_config.get("bootstrap_servers", "localhost:9092"),
                    "sasl_username": self.stream_config.get("sasl_username", "matrice-sdk-user"),
                    "sasl_password": self.stream_config.get("sasl_password", "matrice-sdk-password"),
                    "sasl_mechanism": self.stream_config.get("sasl_mechanism", "SCRAM-SHA-256"),
                    "security_protocol": self.stream_config.get("security_protocol", "SASL_PLAINTEXT"),
                }
            else:  # Redis
                stream_params = {
                    "host": self.stream_config.get("host", "localhost"),
                    "port": self.stream_config.get("port", 6379),
                    "password": self.stream_config.get("password"),
                    "username": self.stream_config.get("username"),
                    "db": self.stream_config.get("db", 0),
                    "connection_timeout": self.stream_config.get("connection_timeout", 120),
                }
            
            # Create and setup stream
            self.stream = MatriceStream(stream_type, **stream_params)
            await self.stream.async_setup(self.input_topic, f"inference_consumer_{self.camera_id}_{self.worker_id}")
            # TODO: Add app name to the consumer group id to make sure it processing once only
            
            self.logger.info(f"Initialized {stream_type.value} stream for consumer worker {self.worker_id}")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize stream for consumer worker: {e}")
            raise

    async def _get_message_safely(self):
        """Safely get message from stream in the current event loop."""
        try:
            if not self.stream:
                self.logger.error("Stream not initialized")
                return None
            return await self.stream.async_get_message(self.message_timeout)
        except Exception as e:
            # Handle stream issues gracefully
            self.logger.debug(f"Error getting message from stream: {e}")
            return None
    
    def _process_message(self, message_data):
        """Process incoming message and add to inference queue."""
        try:
            # Parse message data - handle camera streamer format
            if isinstance(message_data.get("data"), bytes):
                data = json.loads(message_data["data"].decode("utf-8"))
            else:
                data = message_data.get("data", {})
            
            # Handle camera streamer input format
            input_stream = data.get("input_stream", {})
            if not input_stream:
                # Fallback to direct format
                input_stream = data
            
            # Create stream message
            stream_msg = StreamMessage(
                camera_id=self.camera_id,
                message_key=message_data.get("key", data.get("input_name", f"{self.camera_id}_{int(time.time())}")),
                data=data,
                timestamp=datetime.now(timezone.utc),
                priority=1
            )
            
            # Ensure extra_params is a dictionary
            extra_params = data.get("extra_params", {})
            if not isinstance(extra_params, dict):
                self.logger.warning(f"extra_params is not a dict, converting from {type(extra_params)}: {extra_params}")
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

            # Determine frame_id (prefer value from upstream gateway; otherwise fallback to message key)
            frame_id = data.get("frame_id")
            if not frame_id:
                frame_id = message_data.get("key", data.get("input_name", f"{self.camera_id}_{int(time.time() * 1000)}"))

            # Attach frame_id into input_stream for propagation if not present
            try:
                if isinstance(input_stream, dict) and "frame_id" not in input_stream:
                    input_stream["frame_id"] = frame_id
            except Exception:
                pass

            # Create inference task with camera streamer format
            task_data = {
                "message": stream_msg,
                "input_stream": input_stream,  # Pass the full input_stream
                "stream_key": f"{self.camera_id}_{stream_msg.message_key}",
                "extra_params": extra_params,
                "camera_config": self.camera_config.__dict__,
                "frame_id": frame_id
            }
            
            # Add to inference queue with timestamp as tie-breaker for priority queue comparison
            self.inference_queue.put((stream_msg.priority, time.time(), task_data))
            
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse message JSON: {e}")
        except Exception as e:
            self.logger.error(f"Error processing message: {e}")

