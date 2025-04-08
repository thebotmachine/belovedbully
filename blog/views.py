from django.views.generic import ListView, DetailView
from .models import News, Article


class NewsListView(ListView):
    model = News
    template_name = "blog/news_list.html"
    context_object_name = "news"

class NewsDetailView(DetailView):
    model = News
    template_name = "blog/news_detail.html"
    context_object_name = "news"

class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_option = self.request.GET.get("sort", "date_desc")

        if sort_option == "title_asc":
            queryset = queryset.order_by("title")
        elif sort_option == "title_desc":
            queryset = queryset.order_by("-title")
        elif sort_option == "date_asc":
            queryset = queryset.order_by("created_at")
        elif sort_option == "date_desc":
            queryset = queryset.order_by("-created_at")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Статьи'
        return context

    def get_template_names(self):
        if self.request.headers.get("HX-Request"):
            return ['blog/article_list_partial.html']
        return [self.template_name]


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"{self.object.title}"
        return context