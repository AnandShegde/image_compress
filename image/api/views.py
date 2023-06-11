from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def api_hello(request):
    print(request.body)
    return JsonResponse({'message': 'Hello, world!'})