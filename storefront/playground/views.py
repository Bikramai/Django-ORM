from django.shortcuts import render
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem



def say_hello(request):
    # Creating Objects or Inserting Objects 
    # first approach
    collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk=1)
    collection.save()
    

    # Second approach
    # collection = Collection.objects.create(name='a', featured_product_id=1)
    # collection.id
    
       
    return render(request, 'hello.html', {'name': 'Bikram'})
