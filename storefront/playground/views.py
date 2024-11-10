from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer



def say_hello(request):
    # Annotate Objects
    queryset = Customer.objects.annotate(is_new=Value(True))
    
       
    return render(request, 'hello.html', {'name': 'Bikram', 'result': list(queryset)})
