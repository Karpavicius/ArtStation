from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'html/post_list.html', {})
def MarketPlace(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'templates/html/MarketPlace.html', {'post': post})
def Jobs(request, pk):
   	post = get_object_or_404(Post, pk=pk)
    return render(request, 'templates/html/Jobs.html', {'post': post})