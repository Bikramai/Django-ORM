from django.shortcuts import render
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



def say_hello(request):
    # Custom Managers
    TaggedItem.objects.get_tags_for(Product, 1) 
    
       
    return render(request, 'hello.html', {'name': 'Bikram'})
