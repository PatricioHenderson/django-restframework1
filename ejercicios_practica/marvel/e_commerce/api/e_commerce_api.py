from django.db.models import query
from rest_framework.decorators import api_view
from django.http import HttpResponse
from e_commerce.models import *


@api_view(['GET', 'POST'])
def stock(request):
    template = '<h1> The stock of this book is : </h1>'
    return HttpResponse(template)

@api_view(['GET' , 'POST'])
def price(request):
    template = '<h1> The price of this book is :  </h1>'
    return HttpResponse(template)

@api_view(['GET' , 'POST'])
def cart(request):
    comics = []
    for e in Comic.objects.all():
        
        comics.append(e.title)
        
    # queryset = Comic.objects.filter()
    template =f'''
     <h1> You have this books in yout cart :  </h1> 
        <h2>{comics}</h2>
        '''

    return HttpResponse(template )
