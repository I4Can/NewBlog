from django.db import models
from django.utils import timezone
from comment.models import Comment
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.functional import cached_property
from mysite.settings import BASE_DIR
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name="分类标题", max_length=64, unique=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True)
    slug = models.SlugField(max_length=60, default='no-link', unique=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class Tag(models.Model):
    content = models.CharField(max_length=64, verbose_name="标签", unique=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True)
    slug = models.SlugField(max_length=80, default='no-link', unique=True)
    class Meta:
        ordering=['?']

    def __str__(self):
        return self.content


class Article(models.Model):
    title = models.CharField(verbose_name="标题", max_length=64, default="无题")
    views = models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True)
    last_edit_time=models.DateTimeField(verbose_name="修改时间",auto_now=True,null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="所属标签", related_name="sub_articles")
    content = RichTextUploadingField(config_name='my_config')

    def get_absolute_url(self):
        return reverse('blog:article_detail',args=(self.pk,))

    def tag_list(self):
        return ' '.join([tag.content for tag in self.tags.all()])
    class Meta:
        ordering = ['-create_time']

    @cached_property
    def next_article(self):
        return Article.objects.filter(id__lt=self.pk).first()

    @cached_property
    def previous_article(self):
        return Article.objects.filter(id__gt=self.pk).first()

    def views_up(self):
        self.views += 1
        self.save()

    def comment_tree(self):
        parent_comments = Comment.objects.filter(reply_id=None,article_id=self.pk)
        comments_tree = {comment: Comment.objects.filter(reply_id=comment.id).order_by('create_time')
                         for comment in parent_comments}
        return comments_tree



    def __str__(self):
        return self.title


class FriendLink(models.Model):
    name = models.CharField(verbose_name="站点名称", max_length=64, unique=True)
    link = models.URLField(verbose_name="站点链接")
    join_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering=['join_time']
