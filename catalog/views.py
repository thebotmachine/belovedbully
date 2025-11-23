from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from .models import Dog, Litter  # Обновлены импорты моделей
from django.views.generic import ListView, DetailView

class DogFirstImageMixin:
    """
    Миксин для добавления первого изображения каждой собаки в контекст.
    Предполагается, что в шаблоне список объектов доступен под именем 'dogs'.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dogs = context.get('dogs')
        if dogs is not None:
            # Добавляем каждому объекту новое свойство first_image
            for dog in dogs:
                dog.first_image = dog.images.first()  # Работает с универсальной моделью Image
        return context


class DogListView(DogFirstImageMixin, ListView):
    model = Dog
    template_name = 'catalog/dog_list.html'
    context_object_name = 'dogs'
    partial_template_name = 'catalog/dog_list_partial.html'

    category = None
    status_filter = None  # Новый атрибут для фильтрации статуса

    def get_queryset(self):
        queryset = Dog.objects.all()

        if self.category == 'puppy':
            if self.status_filter == 'archive':
                queryset = queryset.filter(status__in=['sold', 'reserved'])
            else:
                status = self.status_filter if self.status_filter else 'available'
                queryset = queryset.filter(status=status)

        if self.category:
            queryset = queryset.filter(category=self.category)

        return self._filter_by_gender(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.category == 'puppy' and self.status_filter == 'sold':
            context['page_title'] = 'Наши выпускники'
        else:
            category_titles = {
                'puppy': 'Свободные щенки',
                'adult': 'Производители',
            }
            context['page_title'] = category_titles.get(self.category, 'Американские булли')
        return context

    def _filter_by_gender(self, queryset):
        gender = self.request.GET.get('gender')
        return queryset.filter(gender=gender) if gender in ['M', 'F'] else queryset

    def get_template_names(self):
        return [self.partial_template_name] if self.request.headers.get("HX-Request") else [self.template_name]


class DogDetailView(DogFirstImageMixin, DetailView):
    model = Dog
    template_name = 'catalog/dog_detail.html'
    context_object_name = 'dog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{self.object.name}"
        return context


class AnnotatedLitterMixin:
    @staticmethod
    def get_annotated_queryset():
        return Litter.objects.annotate(
            puppy_count=Count('puppies'),  # Измените 'dog' на 'puppies'
            male_puppies=Count('puppies', filter=Q(puppies__gender='M')),  # Измените 'dog' на 'puppies'
            female_puppies=Count('puppies', filter=Q(puppies__gender='F'))  # Измените 'dog' на 'puppies'
        )


class LitterListView(AnnotatedLitterMixin, ListView):
    model = Litter
    context_object_name = 'litters'
    template_name = 'catalog/litter_list.html'

    def get_queryset(self):
        return self.get_annotated_queryset().prefetch_related(
            'father__images',
            'mother__images'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Помёты'
        return context


class LitterDetailView(AnnotatedLitterMixin, DetailView):
    model = Litter
    context_object_name = 'litter'
    template_name = 'catalog/litter_detail.html'

    def get_queryset(self):
        return self.get_annotated_queryset().prefetch_related(
            'puppies__images',
            'father__images',
            'mother__images'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Помёт {self.object}"

        # Добавляем щенков в контекст под именем 'dogs'
        context['dogs'] = self.object.puppies.all().prefetch_related('images')

        return context

