from django.contrib import admin
from .models import ( 
	menu_main,
	menu_item
)
# Register your models here.

@admin.register(menu_main)
class MenuMainAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'published')
	list_filter = ('published',)

@admin.register(menu_item)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'name', 'parent', 'menu', 'sort', 'obj_id', 'published')
	list_filter = ('menu', 'parent', 'published')
	search_fields = ('name', 'parent', 'menu')
	save_as = True
	list_editable = ('sort',)
	mptt_level_indent = 20