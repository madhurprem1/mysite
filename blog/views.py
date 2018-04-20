from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('publish_date')
    print posts
    return render(request, 'blog/post_list.html', {'posts': posts})