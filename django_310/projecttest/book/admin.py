from django.contrib import admin

# Register your models here.
from book.models import BookInof,PeopleInfo
admin.site.register(BookInof)
admin.site.register(PeopleInfo)