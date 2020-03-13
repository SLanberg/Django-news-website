from django.contrib import admin
from .models import ( 
	Category,
	Tag,
	Post,
	Commentary,
)


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'creation_date')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Commentary)

