from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from theme_pixel.forms import RegistrationForm, UserLoginForm, UserPasswordResetForm, UserPasswordChangeForm, UserSetPasswordForm
from django.contrib.auth import logout
from .models import Album, Picture, Sitevars


# Create your views here.


# Pages
def index(request):
  return render(request, 'pages/index.html')

def abouts_us(request):
  return render(request, 'pages/about.html')

def contact_us(request):
  return render(request, 'pages/contact.html')

def landing_freelancer(request):
  return render(request, 'pages/landing-freelancer.html')

def blank_page(request):
  return render(request, 'pages/blank.html')

# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
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
  return render(request, 'accounts/sign-up.html', context)

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm


# Components
def accordion(request):
  return render(request, 'components/accordions.html')

def alerts(request):
  return render(request, 'components/alerts.html')

def badges(request):
  return render(request, 'components/badges.html')

def bootstrap_carousels(request):
  return render(request, 'components/bootstrap-carousels.html')

def breadcrumbs(request):
  return render(request, 'components/breadcrumbs.html')

def buttons(request):
  return render(request, 'components/buttons.html')

def cards(request):
  return render(request, 'components/cards.html')

def dropdowns(request):
  return render(request, 'components/dropdowns.html')

def forms(request):
  return render(request, 'components/forms.html')

def modals(request):
  return render(request, 'components/modals.html')

def navs(request):
  return render(request, 'components/navs.html')

def pagination(request):
  return render(request, 'components/pagination.html')

def popovers(request):
  return render(request, 'components/popovers.html')

def progress_bars(request):
  return render(request, 'components/progress-bars.html')

def tables(request):
  return render(request, 'components/tables.html')

def tabs(request):
  return render(request, 'components/tabs.html')

def toasts(request):
  return render(request, 'components/toasts.html')

def tooltips(request):
  return render(request, 'components/tooltips.html')

def typography(request):
  return render(request, 'components/typography.html')




def x(request):
  # Busca todos os álbuns
    vars=Sitevars.objects.filter(page__contains=['index'])
    dc =dict()
    for v in vars:
      dc[v.name]={"content":v.content,
                  "value":v.value}
    albums = Album.objects.all()
    # Para cada álbum, tenta buscar a imagem de capa
    for album in albums:
        album.cover_picture = Picture.objects.filter(album=album, cover=True).first()
        if len(album.description)>= 120:
          album.description = album.description[:120]+"..."
    
    # Renderiza o template com os álbuns e as imagens de capa
    return render(request, 'mypages/main.html', {'albums': albums,'parameters':dc})

def gallerys(request):
  return render(request, 'mypages/gallery.html')

def album(request, album_id):
    # Busca o álbum pelo ID ou retorna um erro 404 se não encontrado
  album = get_object_or_404(Album, id=album_id)
    # Busca todas as imagens associadas ao álbum
  pictures = Picture.objects.filter(album=album_id)
    # Renderiza o template com o álbum e suas imagens
  return render(request, 'mypages/album.html', {'album': album, 'pictures': pictures})

def inside(request):
  return render(request, 'mypages/inside.html')

def listar_imagens(request, album_id):
    # Busca o álbum pelo ID ou retorna um erro 404 se não encontrado
    album = get_object_or_404(Album, id=album_id)
    # Busca todas as imagens associadas ao álbum
    pictures = Picture.objects.filter(album=album_id)
    # Renderiza o template com o álbum e suas imagens
    return render(request, 'mypages/main.html', {'album': album, 'pictures': pictures})