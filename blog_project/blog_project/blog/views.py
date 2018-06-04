from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Import mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



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
    success_url = reverse_lazy('post_list')        # you want to activate when actual delete, hence laze reverse


class DraftListView(LoginRequiredMixin, ListView):
    model = Post

    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


############# COMMENTS #################

@login_required     # make view required by login
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)       # get post or 404 from Post model, where PK is similar

    if request.method == 'POST':        # if someone filled form
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html', {'form' : form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    return redirect('post_detail', pk=pk)