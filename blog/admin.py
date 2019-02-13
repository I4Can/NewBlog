from django.contrib import admin
from comment.admin import CommentInline
# Register your models here.
from .models import *

# class PictureInline(admin.TabularInline):
#     model = Picture
#     extra = 1
#
# class VideoInline(admin.TabularInline):
#     model = Video
#     extra = 1

class TagInline(admin.TabularInline):
    model = Tag
    extra = 0

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'views', 'create_time','last_edit_time','category','tag_list')
    list_filter = ['views', 'create_time']
    filter_horizontal = ('tags',)
    fieldsets = (
        ('article_content',{'fields':('title','content')}),
        ('article_information',{'fields':('views','category','tags')})
    )

class TagAdmin(admin.ModelAdmin):
    list_display = ('content','create_time')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','create_time')
    inlines = [ArticleInline]

class FriendLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'link','join_time')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(FriendLink,FriendLinkAdmin)