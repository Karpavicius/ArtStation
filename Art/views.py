from django.shortcuts import render
from django.utils import timezone
from .models import Post, Artes, Jobs
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ArteForm, JobsForms
from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required

def cadastrarArte(request):
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
        return render(request, 'html/ArtForm.html', {'form': form})

def comprarArte(request, pk):
    arte = Artes.objects.get(pk=pk)
    if arte.comprador == None:
        return render(request, 'html/Arte.html', {'arte':arte})
    return redirect('arts:post_list')

@login_required
def confirmPurchase(request, pk):
    arte = Artes.objects.get(pk=pk)
    arte.comprador = request.user
    arte.save()
    print(request.user.email)
    try:
        send_mail('Purchase confirmed.', 'Thank you for buying on ArtStation', ['evelinksantos@gmail.com'], [request.user.email])
    except BadHeaderError:
        return HttpResponse("Error")
    return redirect('arts:post_list')


def cadastrarJob(request):
    if request.method == "POST":
        form = JobsForms(request.POST, request.FILES)
        if form.is_valid():
            jobs = form.save(commit=False)
            jobs.empresa = request.user
            jobs.published_date = timezone.now()
            jobs.save()
            return redirect('arts:JobsList')
    else:
        form = JobsForms()
        return render(request, 'html/JobsForms.html', {'form': form})

def post_list(request):
    posts = Artes.objects.filter(published_date__lte=timezone.now(), comprador = None).order_by('published_date')
    return render(request, 'html/ArtList.html', {'posts': posts})

def MarketPlace(request):
    marketplace = Artes.objects.filter(comprador = 'null')
    return render(request, 'html/MarketPlace.html', {'marketPlace': marketplace})

def JobsList(request):
    jobs = Jobs.objects.all()
    return render(request, 'html/Jobs.html', {'Jobs': jobs})
    
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