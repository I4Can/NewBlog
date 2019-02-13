from django import template
from blog.models import Category,Tag,FriendLink

register=template.Library()

@register.simple_tag
def get_category():
    return Category.objects.all()

@register.simple_tag
def get_tag():
    return Tag.objects.all()

@register.simple_tag
def get_link():
    return FriendLink.objects.all()[:5]