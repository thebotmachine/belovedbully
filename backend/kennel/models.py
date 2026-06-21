from django.db import models
from slugify import slugify

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Transpose


def dog_media_upload_to(instance, filename):
    dog = instance.dog
    if dog and dog.slug:
        return f'dogs/{dog.slug}/{instance.media_type}s/{filename}'
    return f'dogs/unknown/{instance.media_type}s/{filename}'


class DogSize(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class DogColor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Dog(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Мальчик"
        FEMALE = "female", "Девочка"

    class Status(models.TextChoices):
        FREE = "free", "Свободен"
        RESERVED = "reserved", "Забронирован"
        SOLD = "sold", "Продан"

    class Role(models.TextChoices):
        PUPPY = "puppy", "Щенок"
        PRODUCER = "producer", "Производитель"

    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    name = models.CharField()
    description = models.TextField(blank=True)
    birth_date = models.DateField()

    gender = models.CharField(max_length=10, choices=Gender.choices)
    status = models.CharField(max_length=20, choices=Status.choices, null=True, blank=True, )
    role = models.CharField(max_length=20, choices=Role.choices)

    size = models.ForeignKey(DogSize, on_delete=models.PROTECT)
    color = models.ForeignKey(DogColor, on_delete=models.PROTECT)
    litter = models.ForeignKey('Litter', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='puppies')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class DogMedia(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "image", "Image"
        VIDEO = "video", "Video"

    dog = models.ForeignKey('Dog', on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to=dog_media_upload_to)
    media_type = models.CharField(max_length=10, choices=MediaType, default='image')
    is_cover = models.BooleanField('Обложка', default=False)
    order = models.PositiveIntegerField('Порядок', default=0)

    thumb = ImageSpecField(
        source='file',
        processors=[Transpose(), ResizeToFit(400, 400)],
        format='JPEG',
        options={'quality': 85},
    )
    medium = ImageSpecField(
        source='file',
        processors=[Transpose(), ResizeToFit(800, 800)],
        format='JPEG',
        options={'quality': 85},
    )
    large = ImageSpecField(
        source='file',
        processors=[Transpose(), ResizeToFit(1200, 1200)],
        format='JPEG',
        options={'quality': 90},
    )
    webp = ImageSpecField(
        source='file',
        processors=[Transpose(), ResizeToFit(800, 800)],
        format='WEBP',
        options={'quality': 85},
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['dog'],
                condition=models.Q(is_cover=True),
                name='unique_cover_per_dog'
            )
        ]
        ordering = ['order']

    def __str__(self):
        return f"Медиа для {self.dog.name} ({self.media_type})"

    def save(self, *args, **kwargs):
        if self.is_cover:
            DogMedia.objects.filter(dog=self.dog, is_cover=True).exclude(pk=self.pk).update(is_cover=False)
        super().save(*args, **kwargs)


class Litter(models.Model):
    slug = models.SlugField()
    birth_date = models.DateField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='litters/', blank=True, null=True)

    medium = ImageSpecField(
        source='photo',
        processors=[Transpose(), ResizeToFit(800, 800)],
        format='JPEG',
        options={'quality': 85},
    )


    mother = models.ForeignKey(
        'Dog', on_delete=models.PROTECT, related_name='litters_as_mother'
    )
    father = models.ForeignKey(
        'Dog', on_delete=models.PROTECT, related_name='litters_as_father'
    )


    def __str__(self):
        return f'Помёт {self.mother.name} x {self.father.name} ({self.birth_date})'

