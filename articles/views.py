from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,"articles/article_list.html",{'articles':articles})


def article_detail(request,abc):
    article = Article.objects.get(slug=abc)
    return render(request,"articles/article_detail.html",{'article':article})



@login_required(login_url='/accounts/login/')
def create_article(request):
    return render(request, 'articles/create_article.html')