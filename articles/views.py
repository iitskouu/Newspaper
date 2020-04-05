# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title','body ,')
    template_name = 'article_update.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')