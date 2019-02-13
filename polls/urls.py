from django.urls import path
from .views import *

app_name='polls'
urlpatterns=[
    path('<int:pk>/detail',DetailView.as_view(),name='detail'),
    path('',BaseView.as_view(),name='base'),
    path('<int:question_id>/vote/',vote,name='vote'),
    path('<int:pk>/result/',ResultView.as_view(),name='result'),
]