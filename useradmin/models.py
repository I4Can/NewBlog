from django.db import models

# Create your models here.

class UserInfo(models.Model):
    nickname=models.CharField(verbose_name="昵称",max_length=32,default="nameless")
    username=models.CharField(verbose_name="用户名", max_length=32,unique=True)
    password=models.CharField(verbose_name="密码", max_length=64)
    email=models.EmailField(verbose_name="邮箱",unique=True)
    gender_choice = (
        (1, "男"),
        (0, "女"),
    )
    gender=models.IntegerField(verbose_name="性别",choices=gender_choice,default=0)
    presentation=models.CharField(verbose_name="个人说明",default="你好，陌生人",null=True,blank=True,max_length=240)
    avatar=models.ImageField(verbose_name="头像",default='/media/avatar/HP.jpg',upload_to='media/avatar')
    create_time=models.DateTimeField(verbose_name="注册时间",auto_now_add=True,null=True)