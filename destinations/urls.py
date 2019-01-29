from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.DestinationList.as_view(), name='show_destination'),
    path('destination/<int:pk>/', views.destination_detail, name= 'destination_detail'),
    path('destination/new/', views.new_destination, name ='new_destination'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)