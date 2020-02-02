from django.shortcuts import render, get_object_or_404, redirect
from myblog.models import Post, Comment
from myblog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)

# Create your views here.
# follow CRUD


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        """
        This allows me to use Django ORM when dealing with generic views
        :return: A 'field lookup' - make an SQL query by fetching posts
        by published date which is less than or equal current time (lte)
        and order them by the date descending (dash)
        """
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # login_url, redirect_field_name required for mixin
    login_url = '/login/'
    redirect_field_name = 'myblog/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # login_url, redirect_field_name required for mixin
    login_url = '/login/'
    redirect_field_name = 'myblog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # Reverse_lazy is need for django to actually wait
    # for the post being deleted.
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    # login_url, redirect_field_name required for mixin
    login_url = '/login/'
    redirect_field_name = 'mybolg/post_list.html'
    model = Post

    def get_queryset(self):
        """
        This allows me to use Django ORM when dealing with generic views
        :return: A 'field lookup' - make an SQL query by fetching posts
        if there is no published date (isnull=True) and order them by the
        creation date
        """
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')


################################
################################

#@login_required
def add_comments_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    context_dict = {'form': form}

    return render(request,'myblog/comments_form.html', context_dict)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    # Catch pk in variable because return will not remember it after
    # the post is deleted.
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()

    return redirect('post_detail', pk=pk)