from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'html/post_list.html', {'post': post})

def MarketPlace(request, pk):
    marketplace = get_object_or_404(MarketPlace, pk=pk)
    return render(request, 'html/MarketPlace.html', {'marketPlace': marketPlace})

def Jobs(request, pk):
   	jobs = get_object_or_404(Jobs, pk=pk)
    return render(request, 'html/Jobs.html', {'jobs': jobs})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Art/post_edit.html', {'form': form})