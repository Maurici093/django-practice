from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'destinations_app'
urlpatterns = [
    path('', views.DestinationList.as_view(), name='show_destination'),
    path('login/', views.auth_login, name='authentication'),
    path('signup',views.auth_signup, name='signup'),
    path('logout',views.auth_logout, name='logout'),
    path('destination/<int:pk>/', views.DestinationDetail.as_view(), name= 'destination_detail'),
    path('destination/new/', views.DestinationNew.as_view(), name ='new_destination'),
    path('destination/update/<int:pk>', views.DestinationUpdate.as_view(), name ='update_destination'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)