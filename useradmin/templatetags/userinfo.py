from django import template
from useradmin.models import UserInfo
from useradmin.forms import UserInfoForm
register=template.Library()

@register.filter
def getInfo(username):
    user=UserInfo.objects.filter(username=username).first()
    form=UserInfoForm(instance=user)
    return form