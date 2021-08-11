from django.shortcuts import render
from django.utils import timezone
from .models import Post, Artes, Jobs
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ArteForm, JobsForms, MensagemForms
from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def conta(request):
    a = 2+2
    return JsonResponse(a)

@user_passes_test(lambda u: u.is_superuser)
def cadastrarArte(request):
    if request.method == "POST":
        form = ArteForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('arts:post_list')
    else:
        form = ArteForm()
        return render(request, 'html/ArtForm.html', {'form': form})

@login_required
def comprarArte(request, pk):
    arte = Artes.objects.get(pk=pk)
    if arte.comprador == None:
        return render(request, 'html/Arte.html', {'arte':arte})
    return redirect('arts:post_list')

@login_required
def confirmPurchase(request, pk):
    arte = Artes.objects.get(pk=pk)

    if request.method == "POST":
        if arte.artistas == request.user:
            messages.info(request, 'You can not buy your own art!')
            return redirect('arts:post_list')
        if request.POST.get('email') == request.user.email:
            arte.comprador = request.user
            arte.save()
            print(request.user.email)
            try:
                send_mail('Purchace confimation','Email send. Thank you!', ['evelinksantos@gmail.com'], [request.user.email])
                messages.success(request,'Thank you for buying on ArtStation! ')
            except BadHeaderError:
                return HttpResponse("Error")
        else:
             messages.warning(request,'Email did not match')
    return redirect('arts:post_list')


@user_passes_test(lambda u: u.is_superuser)
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

@login_required
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

@login_required
def EnviarEmail(request):
    mensagemForm = MensagemForms()
    if request.method == "POST":
        try:
            send_mail('Menssage',mensagemForm.mensagem, [mensagemForm.emissor], ['evelinksantos@gmail.com'])
        except BadHeaderError:
            return HttpResponse("Error")
        return redirect()
    return render(request, 'html/formEmail.html', {'email': mensagemForm})

@login_required
def EnviarEmail(request):
    if request.method == 'GET':
        email_form = MensagemForms()
    else:
        email_form = MensagemForms(request.POST)
        if email_form.is_valid():
            emissor = email_form.cleaned_data['emissor']
            assunto = email_form.cleaned_data['assunto']
            msg = email_form.cleaned_data['msg']

            try:
                send_mail(assunto, msg, emissor, ['evelinksantos@gmail.com'])
            except BadHeaderError:
                return render(request, 'html/formEmail.html', {'form': email_form})
            return redirect('MensagemEnviada')
    return render(request, 'html/formEmail.html', {'form': email_form})

def MensagemEnviada(request):
    return render(request, 'html/mensagemObrigado')
