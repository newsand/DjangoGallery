from django.urls import path
from theme_pixel import views
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Pages
    path('', views.index,name='index'),
    path('about-us/', views.abouts_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('blank/', views.blank_page, name='blank'),


    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register, name='register'),
        path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    #meus
    # path('x/', views.x, name='x'),
    path('gallerys/', views.gallerys, name='gallerys'),
    path('album/<int:album_id>', views.album, name='album'),
    path('inside/', views.inside, name='inside'),
    path('imagens/', views.listar_imagens, name='listar_imagens'),
]
