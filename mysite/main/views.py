from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h3>Tech is cool!</h3>")
def v1(response):
    return HttpResponse("<h3>Tech is cooler than it was the last time!</h3>")