from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from theme_pixel.forms import RegistrationForm, UserLoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth import logout
from .models import Album, Picture, Sitevars
from django.contrib.auth.decorators import login_required

# Create your views here.


# Pages
def index(request):
    # Busca todos os álbuns
    vars = Sitevars.objects.filter(page__contains=['index'])
    dc = dict()
    for v in vars:
        dc[v.name] = {"content": v.content,
                      "value": v.value}
    albums = Album.objects.filter(private=False)
    # Para cada álbum, tenta buscar a imagem de capa
    for album in albums:
        album.cover_picture = Picture.objects.filter(album=album, cover=True).first()
        if len(album.description) >= 120:
            album.description = album.description[:120] + "..."

    # Renderiza o template com os álbuns e as imagens de capa
    return render(request, 'mypages/main.html', {'albums': albums, 'parameters': dc})

def abouts_us(request):
  return render(request, 'mypages/about.html')

def contact_us(request):
  return render(request, 'pages/contact.html')


def blank_page(request):
  return render(request, 'pages/blank.html')

# Authentication
class UserLoginView(LoginView):
  template_name = 'myaccounts/sign-in.html'
  form_class = UserLoginForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login')

def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print("Account created successfully!")
      return redirect('/accounts/login')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()

  context = { 'form': form }
  return render(request, 'myaccounts/sign-up.html', context)

class UserPasswordResetView(PasswordResetView):
  template_name = 'myaccounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'myaccounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'myaccounts/password_change.html'
  form_class = UserPasswordChangeForm


# def x(request):
#   # Busca todos os álbuns
#     vars=Sitevars.objects.filter(page__contains=['index'])
#     dc =dict()
#     for v in vars:
#       dc[v.name]={"content":v.content,
#                   "value":v.value}
#     albums = Album.objects.filter(private=False)
#     # Para cada álbum, tenta buscar a imagem de capa
#     for album in albums:
#         album.cover_picture = Picture.objects.filter(album=album, cover=True).first()
#         if len(album.description)>= 120:
#           album.description = album.description[:120]+"..."
#
#     # Renderiza o template com os álbuns e as imagens de capa
#     return render(request, 'mypages/main.html', {'albums': albums,'parameters':dc})

def gallerys(request):
  return render(request, 'mypages/gallery.html')

def album(request, album_id):
    # Busca o álbum pelo ID ou retorna um erro 404 se não encontrado
  album = get_object_or_404(Album, id=album_id)
    # Busca todas as imagens associadas ao álbum
  pictures = Picture.objects.filter(album=album_id)
    # Renderiza o template com o álbum e suas imagens
  return render(request, 'mypages/album.html', {'album': album, 'pictures': pictures})

@login_required(login_url='/accounts/login/') 
def inside(request):
   # Busca todos os álbuns
    vars=Sitevars.objects.filter(page__contains=['index'])
    dc =dict()
    for v in vars:
      dc[v.name]={"content":v.content,
                  "value":v.value}
    albums = Album.objects.filter(private=True)
    # Para cada álbum, tenta buscar a imagem de capa
    for album in albums:
        album.cover_picture = Picture.objects.filter(album=album, cover=True).first()
        if len(album.description)>= 120:
          album.description = album.description[:120]+"..."
    
    # Renderiza o template com os álbuns e as imagens de capa
    return render(request, 'mypages/inside.html', {'albums': albums,'parameters':dc})

def listar_imagens(request, album_id):
    # Busca o álbum pelo ID ou retorna um erro 404 se não encontrado
    album = get_object_or_404(Album, id=album_id)
    # Busca todas as imagens associadas ao álbum
    pictures = Picture.objects.filter(album=album_id)
    # Renderiza o template com o álbum e suas imagens
    return render(request, 'mypages/main.html', {'album': album, 'pictures': pictures})