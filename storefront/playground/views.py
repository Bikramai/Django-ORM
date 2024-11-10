from django.shortcuts import render
from django.db.models import Value, F, Func
from store.models import Product, Customer



def say_hello(request):
    # Annotate Objects
    queryset = Customer.objects.annotate(
        # CONCAT
        full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')
    )
    
       
    return render(request, 'hello.html', {'name': 'Bikram', 'result': list(queryset)})
