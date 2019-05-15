from django.shortcuts import render


# Creating the views
post = [
    {
        'author' : 'CoreyMS'
    }
]

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


