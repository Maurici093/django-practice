from django.contrib import admin
from .models import Destination
# Register your models here.

# admin.site.register(Destination)
@admin.register(Destination)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id','name','category','description','price',)
    list_filter = ('category',)