from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Post # the dot before models means current directory or current application
from django.utils import timezone

def post_list(request):
    # sort posts by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,
                  'blog/post_list.html',    # template
                  {'posts':posts})                       # context, a dictionary of key-values injected into django template for rendering



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    details = Post.objects.filter(pk=pk)
    return render(request,
                  'blog/post_detail.html',
                  {'post':post})



from . forms import PostForm
from django.shortcuts import redirect

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)  # show data in detail_view
                                                        # after post is saved
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})