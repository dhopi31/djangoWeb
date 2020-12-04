from django.contrib import admin

# Register your models here.
from .models import PostProduct, PostImageProduct

class PostImageProductAdmin(admin.StackedInline):
    model = PostImageProduct

@admin.register(PostProduct)
class PostProductAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
        'update',
    ]
    inlines = [PostImageProductAdmin]

    class Meta :
        model = PostProduct

@admin.register(PostImageProduct)
class PostImageProductAdmin(admin.ModelAdmin):
    pass