from django.shortcuts import render

# Create your views here.

from .models import Post # the dot before models means current directory or current application
from django.utils import timezone

def post_list(request):
    # sort posts by published_date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,
                  'blog/post_list.html',    # template
                  {'posts':posts})                       # context, a dictionary of key-values injected into django template for rendering


