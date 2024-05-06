from django.urls import path
from books.views import *

urlpatterns = [
    path("index/",index,name="index"),
    path("test/",test,name="test")
]