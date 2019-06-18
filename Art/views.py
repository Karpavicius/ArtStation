from django.shortcuts import render
from django.utils import timezone
from .models import Post, Artes
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ArteForm
from django.shortcuts import redirect



def cadastrarArte(request):
    if request.method == "POST":
        form = ArteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.artistas = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = ArteForm()
        return render(request, 'html/ArtForm.html', {'form': form})

def comprarArte(request, pk):
    arte = Artes.objects.get(pk=pk)
    if arte.comprador == 'null':
        arte.comprador = request.user
    return redirect('arts:post_list')



def post_list(request):
    posts = Artes.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'html/art_list.html', {'posts': posts})

def MarketPlace(request):
    marketplace = Artes.objects.filter(comprador = 'null')
    return render(request, 'html/MarketPlace.html', {'marketPlace': marketplace})

def Jobs(request, pk):
    jobs = get_object_or_404(Jobs, pk=pk)
    return render(request, 'html/Jobs.html', {'jobs': jobs})
    
def post_new(request):
    if request.method == "POST":
        form = ArteForm(request.POST, request.FILES)
    
        if form.is_valid():
            post = form.save(commit=False)
            post.artistas = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('arts:post_list')
    else:
        form = ArteForm()
    return render(request, 'html/post_edit.html', {'form': form})