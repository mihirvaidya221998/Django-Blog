from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Mihir Sachin Vaidya',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Feb 21, 2024'
    },
    {
        'author': 'Sahil Yadav',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Feb 22, 2024'
    }
]

# Create your views here.
def home(req):
    context = {
        'posts': posts
    }
    return render(req, 'blog/home.html', context)

def about(req):
    return render(req, 'blog/about.html', {'title': 'About'})