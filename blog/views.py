from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request,
                  'blog/post_list.html',    # template
                  {})                       # context, a dictionary of key-values injected into django template for rendering

