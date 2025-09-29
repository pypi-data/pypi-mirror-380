import logging
import threading
import queue


try:
    import redis  # type: ignore
except Exception:  # pragma: no cover
    redis = None  # type: ignore


class RedisFrameCache:
    """Non-blocking Redis cache for frames keyed by frame_id.

    Stores base64 string content under key 'stream:frames:{frame_id}' with field 'frame'.
    Each insert sets or refreshes the TTL.
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: str = None,
        username: str = None,
        ttl_seconds: int = 300,
        prefix: str = "stream:frames:",
        max_queue: int = 10000,
        worker_threads: int = 2,
        connect_timeout: float = 2.0,
        socket_timeout: float = 0.5,
    ) -> None:
        self.logger = logging.getLogger(__name__ + ".frame_cache")
        self.ttl_seconds = int(ttl_seconds)
        self.prefix = prefix
        self.queue: "queue.Queue" = queue.Queue(maxsize=max_queue)
        self.threads = []
        self.running = False
        self._client = None
        self._worker_threads = max(1, int(worker_threads))

        if redis is None:
            self.logger.warning("redis package not installed; frame caching disabled")
            return

        try:
            self._client = redis.Redis(
                host=host,
                port=port,
                db=db,
                password=password,
                username=username,
                socket_connect_timeout=connect_timeout,
                socket_timeout=socket_timeout,
                health_check_interval=30,
                retry_on_timeout=True,
                decode_responses=True,  # store strings directly
            )
        except Exception as e:
            self.logger.warning("Failed to init Redis client: %s", e)
            self._client = None

    def start(self) -> None:
        if not self._client or self.running:
            return
        self.running = True
        for i in range(self._worker_threads):
            t = threading.Thread(target=self._worker, name=f"FrameCache-{i}", daemon=True)
            t.start()
            self.threads.append(t)

    def stop(self) -> None:
        if not self.running:
            return
        self.running = False
        for _ in self.threads:
            try:
                self.queue.put_nowait(None)
            except Exception:
                pass
        for t in self.threads:
            try:
                t.join(timeout=2.0)
            except Exception:
                pass
        self.threads.clear()

    def put(self, frame_id: str, base64_content: str) -> None:
        """Enqueue a cache write for the given frame.

        - frame_id: unique identifier
        - base64_content: base64-encoded image string
        """
        if not self._client or not self.running:
            return
        if not frame_id or not base64_content:
            return
        try:
            key = f"{self.prefix}{frame_id}"
            self.queue.put_nowait((key, base64_content))
        except queue.Full:
            # Drop silently; never block pipeline
            self.logger.debug("Frame cache queue full; dropping frame_id=%s", frame_id)

    def _worker(self) -> None:
        while self.running:
            try:
                item = self.queue.get(timeout=0.5)
            except queue.Empty:
                continue
            if item is None:
                break
            key, base64_content = item
            try:
                # Store base64 string in a Redis hash field 'frame', then set TTL
                # Mimics the Go backend behavior
                self._client.hset(key, "frame", base64_content)
                self._client.expire(key, self.ttl_seconds)
            except Exception as e:
                self.logger.debug("Failed to cache frame %s: %s", key, e)
            finally:
                try:
                    self.queue.task_done()
                except Exception:
                    pass


