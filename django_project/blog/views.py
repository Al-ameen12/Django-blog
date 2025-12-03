'''Using Class Based Views (CBVs)
    import list view from django.views.generic
    create a class named PostList that inherits from ListView
    set the model attribute to Post
    set the template_name attribute to 'blog/home.html'

    changed the template to be used by view to 'blog/home.html'
    set the context_object_name attribute to 'posts' to change the default name of the list object
    order the posts by date_posted in descending order

    imported a DetailView from django.views.generic

    import CreateView from django.views.generic
    created a class named PostCreateView that inherits from CreateView
    set the model attribute to Post
    add the fields attribute to specify the fields to be included in the form for creating a new post
    navigate to urls.py to wire up the new views

    run the server and test the new views by typing the urls in the browser - http://127.0.0.1:8000/post/new/

    error fix: integrity error when creating a post because the author field is missing
    override the form_valid method to set the author of the post to the current logged-in user
    adding the author before the form is submitted and saved to the database

    runserver, test creating a new post again to ensure the integrity error is resolved
   
    error2:no url to redirect to after successfully creating a post
    error2 fix: redirect to the post detail page after successfully creating a post
    navigate to blog/models.py to add get_absolute_url method to Post model

    new error fix: ensure logging in before creating a post
    import LoginRequiredMixin from django.contrib.auth.mixins
    update PostCreateView to inherit from LoginRequiredMixin and CreateView
    this will ensure that only logged-in users can access the post creation view
    testing:users will be redirected to the login page if they try to access the post creation view without being logged in
'''
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
)
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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
