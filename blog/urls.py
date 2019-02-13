"""NewBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from blog.views import *
from django.views.static import serve
from mysite.settings import MEDIA_ROOT
app_name = 'blog'
urlpatterns = [
    path('',SlugList.as_view(),name='index'),
    path('about/',about,name='about'),
    path('archive/',ArchiveList.as_view(),name='archive_list'),
    path('<slug:slug>/',SlugList.as_view(),name='sort_home'),
    path('<slug:slug>/page/<int:page>/', SlugList.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    re_path('^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
]
