from django.contrib import admin
from blog.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    last_display = 'id', 'name,' 'slug',
    last_display_links = 'name',
    search_fields = 'id', 'name,' 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name', ),
    }