from django.urls import path
from .views import DogListView, DogDetailView, LitterListView, LitterDetailView

app_name = 'catalog'

urlpatterns = [
    path('puppies/', DogListView.as_view(category='puppy'), name='puppies_list'),
    path('puppies/archive/', DogListView.as_view(category='puppy', status_filter='sold'), name='puppies_list_archive'),
    path('adults/', DogListView.as_view(category='adult'), name='adults_list'),
    path('dog/<slug:slug>/', DogDetailView.as_view(), name='dog_detail'),
    path('litters/', LitterListView.as_view(), name='litters_list'),
    path('litters/<slug:slug>/', LitterDetailView.as_view(), name='litter_detail'),
]
