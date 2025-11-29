'''Using Class Based Views (CBVs)
    import list view from django.views.generic
    create a class named PostList that inherits from ListView
    set the model attribute to Post
    set the template_name attribute to 'blog/home.html'

    changed the template to be used by view to 'blog/home.html'
    set the context_object_name attribute to 'posts' to change the default name of the list object
    order the posts by date_posted in descending order

    imported a DetailView from django.views.generic
'''
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'home'
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post #it tells the ListView what model to query in other to create the list
    template_name = 'blog/home.html' #specifies the template to be used  <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #this is used to change the default name of the list object from object_list to posts
    ordering = ['-date_posted'] #orders the posts by date_posted in descending order


class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
