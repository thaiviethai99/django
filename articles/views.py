from django.http import HttpResponse
from django.shortcuts import render

def articles_list(request):
    #return HttpResponse('about')
    return render(request,'articles/article_list.html')
