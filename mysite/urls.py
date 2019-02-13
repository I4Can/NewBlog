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
from django.contrib import admin
from django.urls import path, include
import polls.urls, blog.urls, useradmin.urls, comment.urls
from django.conf import settings
from blog.views import MySearchView
from django.conf.urls.static import static

urlpatterns = [
    path('search/', include('haystack.urls'),name='article_search'),
    path('admin/', admin.site.urls),
    path('polls/', include(polls.urls)),
    path('', include(blog.urls)),
    path('useradmin/', include(useradmin.urls)),
    path('comment/', include(comment.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
