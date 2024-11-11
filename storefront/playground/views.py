from django.shortcuts import render
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem



def say_hello(request):
    # Deleting Objects 
    collection = Collection(pk=11)
    collection.delete()
    
    Collection.objects.filter(id__gt=5).delete()


    return render(request, 'hello.html', {'name': 'Bikram'})
