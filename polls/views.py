from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import *
from django.shortcuts import HttpResponse,get_object_or_404,get_list_or_404,HttpResponseRedirect
from django.urls import reverse

class BaseView(generic.ListView):
    template_name='polls/base.html'
    context_object_name='question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name='polls/detail.html'

class ResultView(generic.DetailView):
    model=Question
    template_name='polls/result.html'

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice_id'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"未选中"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result',args=(question_id,)))
