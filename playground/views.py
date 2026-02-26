from django.shortcuts import render
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem

def   say_hello(request):
   
    return render(request, "hello.html", {'name': 'Isaac'}) 
    