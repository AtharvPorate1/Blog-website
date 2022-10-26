from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.article_list,name="list"),
    path('create/',views.create_article,name="create"),
    path('<slug:abc>',views.article_detail, name="detail")


]

