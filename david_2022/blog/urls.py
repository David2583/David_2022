from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("detail/", views.blog_detail, name="blog_detail"),
]
