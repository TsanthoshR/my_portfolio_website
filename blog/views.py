from django.shortcuts import render
from .models import Blog
# Create your views here.
def all_blogs(request):
    Blog_objects = Blog.objects.order_by('-date')[:1]

    return render(request, 'blog/all_blogs.html',{'Blogs':Blog_objects})
