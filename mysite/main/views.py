from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.
def index(response, id):
    ls=ToDoList.objects.get(id=id)
    item=ls.item_set.get(id=1)
    return render(response, "main/base.html",{"name":ls.name, "item":item})
def home(response):
    return render(response, "main/home.html",{"name":"test"}) 
