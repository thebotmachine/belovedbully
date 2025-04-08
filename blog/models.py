import os
import uuid
import math

from django.db import models
from django.utils.text import slugify
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from unidecode import unidecode


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class News(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, blank=True, verbose_name="URL")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to="news_images/", blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Article(TimeStampedModel):
    def get_upload_path(self, filename):
        unique_filename = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        return os.path.join(self.__class__.__name__.lower(), str(self.id), unique_filename)

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(unique=True, blank=True, editable=False, max_length=255, verbose_name="URL")
    content = models.TextField(verbose_name="Содержание")
    image = ProcessedImageField(
        upload_to=get_upload_path,
        processors=[ResizeToFit(1920, 1080)],  # Ограничиваем размер до Full HD (уменьшает файлы)
        format='JPEG',
        options={'quality': 85},  # Сжимаем до 85% качества
        verbose_name="Изображение",
        blank=True, null=True,
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug or Article.objects.filter(pk=self.pk).exclude(title=self.title).exists():
            base_slug = slugify(unidecode(self.title))
            unique_slug = base_slug
            counter = 1

            while Article.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)


    def reading_time(self):
        word_count = len(self.content.split())
        minutes = math.ceil(word_count / 200)
        return minutes

    def __str__(self):
        return self.title


class ArticleImage(TimeStampedModel):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='images')

    def get_upload_path(self, filename):
        unique_filename = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        return os.path.join(self.__class__.__name__.lower(), str(self.article.id), unique_filename)

    image = ProcessedImageField(
        upload_to=get_upload_path,
        processors=[ResizeToFit(1920, 1080)],
        format='JPEG',
        options={'quality': 85},
        verbose_name="Изображение"
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1024, 1024)],
        format='WEBP',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = ArticleImage.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
            except ArticleImage.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Фото {self.article.title}"
