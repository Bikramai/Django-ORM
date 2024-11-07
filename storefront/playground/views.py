from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem



def say_hello(request):
    # Select_related (1)
    # prefetch_related (n)
    queryset = Product.objects.prefetch_related(
        'promotions').select_related('collection').all()
    
       
    return render(request, 'hello.html', {'name': 'Bikram', 'products': queryset})
