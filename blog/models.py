from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(
        verbose_name="Content",
        help_text="Use o editor para adicionar texto e imagens")
    thumbnail = models.ImageField(
        upload_to="blog/thumbnails/",
        null=True,
        blank=True,
        verbose_name="Thumbnail",
        help_text="Imagem de capa do post"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
