from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q, Prefetch

from .models import Dog, Litter, DogMedia
from .serializers import DogListSerializer, DogDetailSerializer, LitterListSerializer, LitterDetailSerializer
from .paginations import DogPagination


class BaseDogListView(ListAPIView):
    serializer_class = DogListSerializer
    pagination_class = DogPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['gender']
    ordering_fields = ['name']
    ordering = ['name']

    def get_queryset(self):
        raise NotImplementedError

    def get_base_queryset(self):
        return (
            Dog.objects
            .prefetch_related(
                Prefetch(
                    'media',
                    queryset=DogMedia.objects.filter(is_cover=True),
                    to_attr='cover_media'
                )
            )
        )


class DogDetailView(RetrieveAPIView):
    queryset = Dog.objects.select_related(
        'size',
        'color',
        'litter',
        'litter__mother',
        'litter__father',
    ).prefetch_related(
        'media'
    )
    serializer_class = DogDetailSerializer
    lookup_field = 'slug'


class PuppyListView(BaseDogListView):
    def get_queryset(self):
        return self.get_base_queryset().filter(
            role='puppy',
            status='free',
        )


class GraduateListView(BaseDogListView):
    def get_queryset(self):
        return self.get_base_queryset().filter(
            role='puppy',
            status='sold',
        )


class ProducerListView(BaseDogListView):
    def get_queryset(self):
        return self.get_base_queryset().filter(
            role='producer',
        )


class LitterListView(ListAPIView):
    queryset = Litter.objects.annotate(puppies_count_db=Count('puppies'),
                                       males_count_db=Count('puppies', filter=Q(puppies__gender='male')),
                                       females_count_db=Count('puppies', filter=Q(puppies__gender='female'))).all()
    serializer_class = LitterListSerializer


class LitterDetailView(RetrieveAPIView):
    queryset = Litter.objects.annotate(puppies_count_db=Count('puppies'),
                                       males_count_db=Count('puppies', filter=Q(puppies__gender='male')),
                                       females_count_db=Count('puppies', filter=Q(puppies__gender='female'))).all()
    serializer_class = LitterDetailSerializer
    lookup_field = 'slug'
