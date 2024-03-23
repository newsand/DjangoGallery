from django.contrib import admin
from .models import Picture, Album, Sitevars

class PicturesAdmin(admin.ModelAdmin):
    list_display = ('title','cover','album',)
    search_fields = ['title','cover']
    list_filter = ('album', )

admin.site.register(Picture, PicturesAdmin)

class AlbumnsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    list_filter = ('private', )

admin.site.register(Album, AlbumnsAdmin)

class SitevarsAdmin(admin.ModelAdmin):
    list_display = ('name','value','page')
    search_fields = ['name']

admin.site.register(Sitevars, SitevarsAdmin)
