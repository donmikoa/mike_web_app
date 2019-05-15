from django.shortcuts import render


# Creating the views
post = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    }
]

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


