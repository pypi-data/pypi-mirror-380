import time
import functools

class RateLimiter:
    def __init__(self, max_requests=5, period=60, redis_client=None, identifier_func=None, error_handler=None):
        """
        Generic Rate Limiter (framework-agnostic).
        
        :param max_requests: Allowed requests in the period
        :param period: Time window in seconds
        :param redis_client: Optional Redis client (shared store)
        :param identifier_func: Function(request) -> str (user ID or IP)
        :param error_handler: Function() -> error response (framework-specific)
        """
        self.max_requests = max_requests
        self.period = period
        self.redis = redis_client
        self.identifier_func = identifier_func or (lambda request: "global")
        self.error_handler = error_handler or (lambda: ("Too Many Requests", 429))
        self.memory_store = {}

    def is_allowed(self, identifier: str) -> bool:
        now = time.time()
        if self.redis:
            # Redis backend
            key = f"rate:{identifier}"
            pipeline = self.redis.pipeline()
            pipeline.zadd(key, {now: now})
            pipeline.zremrangebyscore(key, 0, now - self.period)
            pipeline.zcard(key)
            pipeline.expire(key, self.period)
            _, _, count, _ = pipeline.execute()
            return count <= self.max_requests
        else:
            # In-memory backend
            if identifier not in self.memory_store:
                self.memory_store[identifier] = []
            self.memory_store[identifier] = [
                t for t in self.memory_store[identifier] if now - t < self.period
            ]
            if len(self.memory_store[identifier]) >= self.max_requests:
                return False
            self.memory_store[identifier].append(now)
            return True

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(request=None, *args, **kwargs):
            identifier = self.identifier_func(request)
            if not self.is_allowed(identifier):
                return self.error_handler()
            return func(request, *args, **kwargs)
        return wrapper

