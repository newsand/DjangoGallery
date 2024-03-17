from django.contrib import admin
from .models import Picture, Album

class PicturesAdmin(admin.ModelAdmin):
    list_display = ('title','cover','album',)
    search_fields = ['title','cover']

admin.site.register(Picture, PicturesAdmin)

class AlbumnsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']

admin.site.register(Album, AlbumnsAdmin)
