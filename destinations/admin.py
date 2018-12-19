from django.contrib import admin
from .models import Destination, Favorite
# Register your models here.

# admin.site.register(Destination)
@admin.register(Destination)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id','name','category','description','price',)
    list_filter = ('category',)

@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('user', 'destination',)
    list_filter = ('user', 'destination',)
