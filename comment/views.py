from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from comment.forms import CommentForm
from django.views.generic.edit import FormView
from django.urls import reverse
from comment.models import Comment

class CommentView(FormView):
    form_class = CommentForm
    template_name = 'blog/article_page.html'
    def form_valid(self, form):
        user_id=self.request.session.get('user_id', None)
        article_id=self.kwargs.get('article_id')
        comment_id = form.cleaned_data.get('parent_comment_id')
        new_comment=Comment.objects.create(content=form.cleaned_data.get('content'),deliver_id=user_id,reply_id=comment_id,article_id=article_id)
        if comment_id is '':
            comment_id=new_comment.id
        self.success_url = '{article_url}#comment_{comment_id}'.format(
            article_url=reverse("blog:article_detail", args=(self.kwargs['article_id'],)), comment_id=comment_id)
        return super().form_valid(form)
