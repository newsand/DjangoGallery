from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),           # Lista de posts
    path('<int:pk>/', views.post_detail, name='post_detail'),  # Detalhe do post
]