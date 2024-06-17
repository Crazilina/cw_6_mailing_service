from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = RichTextUploadingField(verbose_name="Содержимое статьи")
    image = models.ImageField(upload_to='blog_images/', verbose_name="Изображение", blank=True, null=True)
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    publication_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
