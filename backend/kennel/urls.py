from django.urls import path
from .views import DogDetailView, PuppyListView, ProducerListView, GraduateListView, LitterDetailView, LitterListView

urlpatterns = [
    path('dogs/<slug:slug>/', DogDetailView.as_view()),
    path('puppies/', PuppyListView.as_view()),
    path('producers/', ProducerListView.as_view()),
    path('graduates/', GraduateListView.as_view()),
    path('litters/<slug:slug>/', LitterDetailView.as_view()),
    path('litters/', LitterListView.as_view()),
]
