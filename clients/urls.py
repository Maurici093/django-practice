from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('clients/', views.show_client, name='show_client'),
    path('client/new/', views.new_client, name= 'new_client'),
    ]