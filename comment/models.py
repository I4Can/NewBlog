from django.db import models
from useradmin.models import UserInfo
# Create your models here.

class Comment(models.Model):
    content = models.TextField(verbose_name="评论内容")
    deliver = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="user_comments")
    reply = models.ForeignKey("self", on_delete=models.CASCADE, related_name="all_replies", null=True, default=None,
                              blank=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    article=models.ForeignKey('blog.Article',on_delete=models.CASCADE,related_name="article_comments",default=None,null=True,blank=True)

    class Meta:
        ordering=['-create_time']