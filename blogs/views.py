from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts = [
    # dictionary
    {
        'author': 'Olo Panganiban',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27 2020',
    },
    {
        'author': 'John Wick',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28 2020',
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html', {})
