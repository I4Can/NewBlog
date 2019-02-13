from django.shortcuts import render,HttpResponse
from django.views.decorators.http import require_http_methods
from useradmin.models import UserInfo
from django.views.generic.edit import UpdateView
import json
# Create your views here.

class UserUpdateView(UpdateView):
    model = UserInfo
    fields = ['avatar', 'nickname', 'gender', 'presentation']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        self.success_url=self.kwargs.get('request_url','/')
        return self.success_url

def login(request):
    if request.method == 'GET':
        return render(request, 'useradmin/sign.html')
    else:
        ret = {'status': False, 'msg': '用户名或密码错误'}
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            obj = UserInfo.objects.filter(username=username, password=password).first()
            if obj:
                request.session.flush()
                request.session['username'] = obj.username
                request.session['user_id'] = obj.id
                request.session.set_expiry(60 * 60 * 24 * 30)
                ret['msg'] = "登录成功"
                ret['status'] = True
        except Exception as  e:
            ret['msg'] = str(e)
        return HttpResponse(json.dumps(ret))

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        ret={'status': True, 'msg': None}
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            UserInfo.objects.create(username=username, password=password, email=email)
            """
                传到后台
                ORM
                返回登陆页面
            """
            obj = UserInfo.objects.filter(username=username, password=password).first()
            request.session['username'] = obj.username
            request.session['user_id'] = obj.id
        except Exception as e:
            print(str(e))
            ret['msg'] = str(e)
            ret['status']=False
        return HttpResponse(json.dumps(ret))

@require_http_methods(['POST'])
def check_username(request):
    ret = {'status': True, 'massage': None}
    username = request.POST.get('username')
    obj = UserInfo.objects.filter(username=username)
    if obj:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))

def check_email(request):
    ret = {'status': True, 'massage': None}
    email = request.POST.get('email')
    obj = UserInfo.objects.filter(email=email)
    if obj:
        ret['status'] = False
    return HttpResponse(json.dumps(ret))

@require_http_methods(["POST"])
def logout(request):
    if request.POST.get('username',None)==request.session.get('username'):
        request.session.flush()
        return HttpResponse("登出成功")
    else:
        return HttpResponse("登出失败")