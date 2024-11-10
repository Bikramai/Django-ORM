from django.shortcuts import render
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



def say_hello(request):
    # Querying Generic Relationships
    content_type = ContentType.objects.get_for_model(Product)

    queryset = TaggedItem.objects \
        .select_related('tag') \
        .filter(
            content_type=content_type, 
            object_id=1
        )
    
       
    return render(request, 'hello.html', {'name': 'Bikram', 'result': list(queryset)})
