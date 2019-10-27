from .models import Post
from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Post)