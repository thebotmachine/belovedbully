from django.views.generic import TemplateView
from catalog.models import Dog
from info.models import FAQ


class MainPageView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        puppies = Dog.objects.filter(category='puppy')[:4]
        adults = Dog.objects.filter(category='adult')[:4]
        faqs = FAQ.objects.all()

        context['puppies'] = puppies
        context['adults'] = adults
        context['faqs'] = faqs
        return context