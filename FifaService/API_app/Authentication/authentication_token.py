import os
from django.http import HttpResponse
from rest_framework import status


#starts and configures
class TokenAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    #this code is executed on every request, the response after
    def __call__(self, request):
        apiKey = os.getenv('API_KEY')
        if apiKey != None:
            if not('x-api-key' in request.headers and request.headers['x-api-key'] == str(apiKey)):
                return HttpResponse({'Unauthorized': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        response = self.get_response(request)        

        return response