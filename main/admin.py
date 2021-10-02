from django.contrib import admin
from .models import Posts

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ("created_at", )

admin.site.register(Posts, PostsAdmin)