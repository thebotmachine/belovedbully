import os
import uuid

from dateutil.relativedelta import relativedelta
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from datetime import date
from babel.dates import format_date
from django.utils.translation import ngettext
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from unidecode import unidecode
from django.db.models.signals import pre_delete

GENDER_CHOICES = (
    ('M', 'Кобель'),
    ('F', 'Сука'),
)

STATUS_CHOICES = (
    ("available", "Свободен"),
    ("reserved", "Забронирован"),
    ("sold", "Куплен"),
)

CATEGORY_CHOICES = (
    ('puppy', 'Щенок'),
    ('adult', 'Производитель'),
)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class Dog(TimeStampedModel):
    name = models.CharField("Имя", max_length=20)
    slug = models.SlugField("URL", unique=True, blank=True, editable=False)
    category = models.CharField("Категория", max_length=10, choices=CATEGORY_CHOICES)
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES, null=True,)
    description = models.TextField("Описание", blank=True, null=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField("Пол", max_length=1, choices=GENDER_CHOICES)
    color = models.CharField("Окрас", max_length=100, null=True, blank=True)
    pedigree = models.URLField("Родословная", max_length=500, null=True, blank=True)
    dog_type = models.CharField("Тип", max_length=100, null=True, blank=True)
    litter = models.ForeignKey('Litter',on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Помёт")
    price = models.DecimalField("Стоимость", max_digits=10, decimal_places=2, null=True, blank=True)

    def get_age(self):
        """
        Возвращает возраст собаки в формате "X год/года/лет Y месяц/месяца/месяцев".
        Если дата рождения не указана, возвращает None.
        Если возраст менее месяца, выводит количество дней.
        """
        if not self.birth_date:
            return None

        today = date.today()
        age = relativedelta(today, self.birth_date)
        years, months = age.years, age.months

        # Если меньше месяца, выводим количество дней
        if years == 0 and months == 0:
            days = (today - self.birth_date).days
            return f"{days} д."  # "д." обозначает дни

        def declension_years(years: int) -> str:
            return f"{years} г." if years % 10 in (1, 2, 3, 4) and not (11 <= years % 100 <= 14) else f"{years} л."

        def declension_months(months: int) -> str:
            return f"{months} м."

        parts = []
        if years:
            parts.append(declension_years(years))
        if months:
            parts.append(declension_months(months))

        return " ".join(parts)

    def save(self, *args, **kwargs):
        if self.category == "adult":
            self.status = None
            self.litter = None
            self.price = None

        if not self.slug or Dog.objects.filter(pk=self.pk).exclude(name=self.name).exists():
            base_slug = slugify(unidecode(self.name))
            unique_slug = base_slug
            counter = 1

            while Dog.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name


class DogImage(TimeStampedModel):
    dog = models.ForeignKey('Dog', on_delete=models.CASCADE, related_name='images')

    def get_upload_path(self, filename):
        unique_filename = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        return os.path.join(self.__class__.__name__.lower(), str(self.dog.id), unique_filename)

    image = ProcessedImageField(
        upload_to=get_upload_path,
        processors=[ResizeToFit(1920, 1080)],
        format='JPEG',
        options={'quality': 85},
        verbose_name="Изображение"
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 600)],
        format='WEBP',
    )

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = DogImage.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
            except DogImage.DoesNotExist:
                pass
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)


    class Meta:
        ordering = ['-id']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"{self.dog.name}"

@receiver(pre_delete, sender=Dog)
def delete_dog_images(sender, instance, **kwargs):
    """
    Удаляет все связанные изображения при удалении собаки.
    Вызывает метод delete() каждого изображения для очистки файлов.
    """
    for image in instance.images.all():
        image.delete()


class Litter(TimeStampedModel):
    father = models.ForeignKey(
        Dog,
        on_delete=models.SET_NULL,
        null=True,
        related_name='father_litters',
        verbose_name="Отец",
        limit_choices_to={'gender': 'M', 'category': 'adult'},
    )
    mother = models.ForeignKey(
        Dog,
        on_delete=models.SET_NULL,
        null=True,
        related_name='mother_litters',
        verbose_name="Мать",
        limit_choices_to={'gender': 'F', 'category': 'adult'},
    )
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    slug = models.SlugField("URL", unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Litter.objects.get(pk=self.pk)
            if (self.father != old_instance.father or
                self.mother != old_instance.mother or
                self.birth_date != old_instance.birth_date):
                self.slug = None

        if not self.slug:
            base_slug = slugify(f"{self.father.name} × {self.mother.name} {self.birth_date}")
            unique_slug = base_slug
            counter = 1

            while Litter.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Помёт"
        verbose_name_plural = "Помёты"

    def __str__(self):
        return f"{self.father.name} × {self.mother.name} {self.birth_date}"


class LitterImage(TimeStampedModel):
    litter = models.ForeignKey('Litter', on_delete=models.CASCADE, related_name='images')

    def get_upload_path(self, filename):
        unique_filename = f"{uuid.uuid4().hex}{os.path.splitext(filename)[1]}"
        return os.path.join(self.__class__.__name__.lower(), str(self.litter.id), unique_filename)

    image = ProcessedImageField(
        upload_to=get_upload_path,
        processors=[ResizeToFit(1920, 1080)],
        format='JPEG',
        options={'quality': 85},
        verbose_name="Изображение"
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 600)],
        format='WEBP',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = LitterImage.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    if os.path.isfile(old_instance.image.path):
                        os.remove(old_instance.image.path)
            except LitterImage.DoesNotExist:
                pass
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Фото {self.litter}"


@receiver(pre_delete, sender=Litter)
def delete_litter_images(sender, instance, **kwargs):
    """
    Удаляет все связанные изображения при удалении собаки.
    Вызывает метод delete() каждого изображения для очистки файлов.
    """
    for image in instance.images.all():
        image.delete()