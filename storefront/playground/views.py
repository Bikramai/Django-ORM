from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):

    queryset = Product.objects.values('id', 'title', 'collection__title')
    
        
    return render(request, 'hello.html', {'name': 'Bikram', 'products': queryset})
