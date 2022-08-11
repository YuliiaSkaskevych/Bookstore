from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000000)

    def __str__(self):
        return self.name


class Quote(models.Model):
    message = models.CharField(max_length=10000000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Author: {self.author}'
