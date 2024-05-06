from django.urls import path
from book.views import *
urlpatterns = [
    path('create/',createbook),
    path('<city_id>/<shop_id>',shop)  # 获取路径中的参数
]
