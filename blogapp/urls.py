from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:slug>', CategoryBlog.as_view(), name='category_blog'),
    path('tag/<slug:slug>', TagBlog.as_view(), name='tag_blog'),
    path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),

    # path('search/', SearchView.as_view(), name = 'search'),
  
    path('loyiha/', loyiha_list, name = 'loyiha'),
]