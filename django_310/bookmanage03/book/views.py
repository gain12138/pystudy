from django.http import HttpResponse
from django.shortcuts import render

from book.models import BookInfo


# Create your views here.
def createbook(request):
    # book = BookInfo.objects.create(
    #     name='abc',
    #     pub_date='2000-1-1',
    #     readcount=1
    # )
    return HttpResponse("Hello world")

def shop(request,city_id,shop_id):
    print (city_id,shop_id)
    query = request.GET
    print(query['id'])
    return HttpResponse(query['id'])