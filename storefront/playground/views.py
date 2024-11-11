from django.shortcuts import render
from django.db.models import Value, F, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from django.db import connection, transaction
from store.models import Product, Collection, Order, OrderItem
from tags.models import TaggedItem


def say_hello(request):
    # Executing Raw SQL Queries
    with connection.cursor() as cursor:
        cursor.callproc('get_customers', [1, 2, 'a'])

    return render(request, 'hello.html', {'name': 'Bikram'})
