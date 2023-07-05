from django.contrib import admin
# Register your models here.
from .models import Post, Comment, MarkPost, MarkComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created']
    list_filter = ['created', 'updated']
    search_fields = ['author', 'body']

admin.site.register(MarkPost)
admin.site.register(MarkComment)
