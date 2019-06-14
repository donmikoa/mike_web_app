from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Creating the views
posts = [
    {
        'author': 'Michael',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Deji Iyaomolere',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


# Creating functions for home.html and about.html
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


