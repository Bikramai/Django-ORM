from django.shortcuts import render
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from store.models import Product, Customer



def say_hello(request):
    # Annotate Objects
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    )
    
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Concat('first_name', Value(' '), 'last_name')
    )
       
    return render(request, 'hello.html', {'name': 'Bikram', 'result': list(queryset)})
