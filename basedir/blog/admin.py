from django.contrib import admin

# Register your models here.
from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update',
    ]
    inlines = [PostImageAdmin]

    class Meta :
        model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Post, PostAdmin)