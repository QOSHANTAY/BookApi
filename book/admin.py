from django.contrib import admin
from .models import Book,Authors,Category
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','category','pages','price']
    list_display_links = ['title']
    list_editable = ['price']
    search_fields = ['title']
    list_filter = ['author','category']
admin.site.register(Book,BookAdmin)

class AuthorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('auth_name',)
    }
admin.site.register(Authors,AuthorsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('category_name',)
    }
admin.site.register(Category,CategoryAdmin)

