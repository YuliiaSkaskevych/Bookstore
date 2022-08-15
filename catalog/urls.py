from django.urls import path

from .views import create_reminder, quote_list
from . import views

app_name = 'catalog'
urlpatterns = [
    path('reminder/', create_reminder, name="create_reminder"),
    path('quotes/', quote_list, name='pagination_quotes'),
    path('authors/', views.AuthorListView.as_view(), name='pagination_authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='detail_author')
    ]
