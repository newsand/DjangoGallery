from django.db import models
from django.contrib.postgres.fields import ArrayField
from core import settings


class Album(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)  # Usando TextField para descrições mais longas
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to='imagens/')
    # O 'upload_to' define o subdiretório dentro de MEDIA_ROOT onde as imagens serão salvas
    album = models.ForeignKey(
        "Album",
        on_delete=models.CASCADE,
        blank = True,
        null = True,
    )
    cover = models.BooleanField(default=False,null=False,blank=False)
    

    def __str__(self):
        return f"{self.title} {self.album.id if self.album else ''} {'Capa' if self.cover else 'Não é capa'}"
    @classmethod
    def get_media_path(cls):
        return settings.MEDIA_ROOT

class Sitevars(models.Model):
    name = models.CharField(max_length=100)
    page = ArrayField(models.CharField(max_length=100))
    value = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    def to_json(self):
        return {name:self.name,
                value:self.value,
                content:self.content}