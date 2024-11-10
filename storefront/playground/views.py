from django.shortcuts import render
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Product, Customer



def say_hello(request):
    # Expression Wrappers
    discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    
    queryset = Product.objects.annotate(
        discounted_price=discounted_price
    )
       
    return render(request, 'hello.html', {'name': 'Bikram', 'result': list(queryset)})
