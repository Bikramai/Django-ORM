from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):
    # Products: inventory < 10 AND Price < 20
    queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    
        
    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
