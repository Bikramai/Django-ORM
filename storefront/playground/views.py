from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Order



def say_hello(request):
    # Select_related (1)
    # prefetch_related (n)
    queryset = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    
       
    return render(request, 'hello.html', {'name': 'Bikram', 'orders': queryset})
