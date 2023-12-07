# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.show_search_page, name='search_page'),
    path('api/search/<str:file_name>/<str:search_value>/', views.search_api, name='api_search'),
]
