from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Import mixins
from django.contrib.auth.mixins import LoginRequiredMixin



class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    # Create generic view. 
    # With get_queryset you are doing query on model (choosen)
    # Grap postm model, all object, and filter out based on conditions.
    # __lte is conditions (less than or equat to)
    # order by published_date (- means descending order)
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


# Add mixing for login required to create post
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post

    # required for mixing
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post

    # required for mixing
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = rreverse_lazy('post_list')        # you want to activate when actual delete, hence laze reverse


class DraftListView(LoginRequiredMixin, ListView):
    model = Post

    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')