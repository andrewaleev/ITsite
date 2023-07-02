from django.contrib import admin
# Register your models here.
from .models import Post, Comment, MarkPost, MarkComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Comment)
admin.site.register(MarkPost)
admin.site.register(MarkComment)
