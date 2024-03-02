
from datetime import datetime, time
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class AvailableMiddleware(MiddlewareMixin):
    def process_request(self, request):
        present = datetime.now().time()
        begin_time = time(15, 0)
        end_time = time(20, 0)

        if not ((begin_time <= present) and (end_time >= present)):
            return
        return HttpResponseForbidden(f"it will be active between {begin_time} and {end_time}.")
