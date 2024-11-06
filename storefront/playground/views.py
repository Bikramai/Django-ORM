from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):
    # Keyword=value, range,
    queryset = Product.objects.filter(collection__id__range=(1, 2, 3))
    
        
    return render(request, 'hello.html', {'name': 'Bikram', 'products': list(queryset)})
