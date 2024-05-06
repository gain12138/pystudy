from django.db import models


class BookInof(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInof, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
