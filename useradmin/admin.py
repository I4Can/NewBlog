from django.contrib import admin
from useradmin.models import UserInfo
from comment.models import Comment
from comment.admin import CommentInline
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('nickname','username','gender','presentation','create_time','email')
    list_filter = ['create_time','gender']


admin.site.register(UserInfo,UserAdmin)