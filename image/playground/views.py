from django.shortcuts import render
import os

def say_hello(request):
    print(os.listdir('.'))
    y = 10

    return render(request, 'hello.html')
