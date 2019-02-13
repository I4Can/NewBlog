from django.contrib import admin
from comment.models import Comment
# Register your models here.
class CommentInline(admin.TabularInline):
    model=Comment
    extra = 0

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content','deliver','create_time','article')

admin.site.register(Comment,CommentAdmin)