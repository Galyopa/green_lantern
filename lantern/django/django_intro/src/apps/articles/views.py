from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView

from apps.articles.forms import SearchForm, ArticleForm
from apps.articles.models import Article


def main_page(request):
    return render(request, 'pages/main_page.html')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        # form = SearchForm(data=request.GET)
        search_q = request.GET.get('search', '')
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {
            'articles': articles,
            # 'search_form': form
        }
        return render(request, 'pages/search.html', context=context_data)


class ArticlesView(FormView):
    template_name = 'pages/articles_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('articles:success_url')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArticlesListView(ListView):
    model = Article
    template_name = 'pages/articles_page_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    queryset = Article.objects.all()
