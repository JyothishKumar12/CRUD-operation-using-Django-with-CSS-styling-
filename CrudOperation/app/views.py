from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def show(request):
    return HttpResponse('<h1>haiiii</h1>')