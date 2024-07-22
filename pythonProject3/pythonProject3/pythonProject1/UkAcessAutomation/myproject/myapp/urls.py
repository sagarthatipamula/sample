# myapp/urls.py
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search/', views.show_search_page, name='search_page'),
    path('api/search/<str:file_name>/<str:search_value>/', views.search_api, name='api_search'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('login/', views.show_login_page, name='login_page'),
    path('accounts/login/', views.login_user, name='login_user'),
    path('get_folder_names/', views.get_folder_names, name='get_folder_names')
]
