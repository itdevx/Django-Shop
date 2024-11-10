from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"Reuquest Methode : {request.method}")
        print(f"Requets URL : {request.get_full_path()}")

    def process_response(self, request, response):
        print(f"Response status code {response.status_code}")
        return response