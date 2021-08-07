from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def all_blogs(request):
    Blog_objects = Blog.objects.order_by('-date') #[:2]

    return render(request, 'blog/all_blogs.html',{'Blogs':Blog_objects})

def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    dict_to_pass={'blog_id':blog_id,
                  'blog':blog,
                    }
    return render(request, 'blog/details.html',dict_to_pass)
