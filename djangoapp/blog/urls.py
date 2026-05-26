from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('page/<slug:slug>/', page, name='page'),
    path('post/<slug:slug>/', post, name='post'),
    path('created_by/<int:author_pk>/', created_by, name='created_by'),
    path('category/<slug:slug>/', category, name='category'),
    path('tag/<slug:slug>/', tag, name='tag'),
]
