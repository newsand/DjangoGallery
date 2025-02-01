from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Colunas na lista
    search_fields = ('title', 'content')                  # Campos pesquisáveis
    list_filter = ('created_at',)                        # Filtros laterais
    date_hierarchy = 'created_at'                        # Navegação por data
    
    # Campos organizados em grupos no formulário
    fieldsets = (
        ('Conteúdo', {
            'fields': ('title','subtitle', 'content', 'thumbnail')
        }),
    )