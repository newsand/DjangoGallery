# core URL Configuration

# Importações necessárias do Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Lista de padrões de URL que direciona URLs para as views correspondentes
urlpatterns = [
    # Inclui as URLs da aplicação 'home'
    path('', include('home.urls')),
    
    # URL do admin do Django
    path("admin/", admin.site.urls),
    
    # Inclui as URLs da aplicação 'theme_pixel'
    path("", include('theme_pixel.urls')),
    # ... suas outras urls
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
