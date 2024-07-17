import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body #byte string of JSON data
    print(body)
    return JsonResponse({"message":"Hi there"})