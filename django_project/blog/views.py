from django.shortcuts import render


posts = [
    {
        'author': 'Al-ameen',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2024'
    }
]

def home(request):
    context = {
        'posts' : posts,
        'title' : 'home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
