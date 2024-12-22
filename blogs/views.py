from django.shortcuts import render
from django.views import generic
from .models import Blogs
# Create your views here.
class BlogsList(generic.ListView):
    model = Blogs
    template_name = 'blogs/blogs_list.html'
    context_object_name = 'blogs'

class BLogDetail(generic.DetailView):
    model = Blogs
    template_name = 'blogs/blogs_detail.html'
    context_object_name = 'blog'