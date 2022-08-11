from django.contrib import admin

from .models import Author, Quote


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    fields = ['name', 'description']
    search_fields = ["name"]


@admin.register(Quote)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['message', 'author']
    fields = ['message', 'author']
    raw_id_fields = ['author', ]
