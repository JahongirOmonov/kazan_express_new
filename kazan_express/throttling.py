from rest_framework.throttling import AnonRateThrottle
from datetime import datetime, time


class BlockThrottle(AnonRateThrottle):
    def allow_request(self, request, view):
        current_time=datetime.now().time()
        print(current_time)

        begin_time = time(15, 0)
        end_time = time(16, 0)

        if not ((begin_time <= current_time) and (end_time >= current_time)):
            return super().allow_request(request, view)
        return True
