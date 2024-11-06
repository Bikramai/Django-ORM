from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):
    # Products: inventory = price
    queryset = Product.objects.order_by('unit_price', '-title').reverse()
    
        
    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
