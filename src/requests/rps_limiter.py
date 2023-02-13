import time


# Singleton
class RpsLimiter(object):
    TIME_BETWEEN_REQUESTS = 0.5

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RpsLimiter, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.previous_request_time = 0

    def wait_till_next_available_request(self):
        time_to_wait = max(
            self.previous_request_time + self.TIME_BETWEEN_REQUESTS - time.time(),
            0,
        )
        self.previous_request_time = time.time()
        time.sleep(time_to_wait)

