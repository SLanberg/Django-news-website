from django.contrib import admin
from .models import ( 
	menu_main,
	menu_item
)
# Register your models here.

admin.site.register(menu_main)
admin.site.register(menu_item)