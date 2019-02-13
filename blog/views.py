from django.shortcuts import render
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_http_methods
from blog.models import Article
from django.shortcuts import render
from comment.forms import CommentForm
import re
# Create your views here.
class ArticleList(ListView):
    context_object_name = 'article_list'
    paginate_by = 6
    template_name = 'blog/articles.html'
    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class SlugList(ArticleList):
    def get_queryset(self):
        slug = self.kwargs.get('slug',None)
        article_list = Article.objects.filter(tags__slug=slug).all()
        if not article_list:
            article_list = Article.objects.filter(category__slug=slug).all()
        if not article_list:
            article_list = Article.objects.all()
        # articles = [{
        #     'id': str(article.id),
        #     'title': article.title,
        #     'views': article.views,
        #     'category': article.category.title,
        #     'content': article.content,
        #     'create_time': article.create_time.strftime("%m-%d,%Y/%H:%M"),
        # } for article in article_list
        # ]
        return article_list

class ArchiveList(ArticleList):
    template_name = 'blog/archive.html'
    context_object_name = 'date_dict'
    paginate_by = None
    def get_queryset(self):
        article_list=Article.objects.all()
        date_sorted_articles = {}
        for article in article_list:
            date = article.create_time.strftime("%Y-%m").split("-")
            date_sorted_articles.setdefault(date[0], {}).setdefault(
                date[1] if int(date[1]) > 10 else date[1][1:2], []).append(article)
        return date_sorted_articles

class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_page.html'
    context_object_name = 'article'
    def get(self, request, *args, **kwargs):
        response=super(ArticleDetail,self).get(request,*args,**kwargs)
        self.object.views_up()
        return response

    def get_context_data(self, **kwargs):
        comment_form=CommentForm()
        kwargs['form']=comment_form
        return super(ArticleDetail,self).get_context_data(**kwargs)

def about(request):
    return render(request,'blog/about.html')


from haystack.generic_views import SearchView

class MySearchView(SearchView):
    """My custom search view."""

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        # further filter queryset based on some set of criteria
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        return context