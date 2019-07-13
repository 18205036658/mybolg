from django.contrib import admin

# Register your models here.
from .models import Post,Category,Tag

class PostAdmin(admin.ModelAdmin):
	list_display = ['id','title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)