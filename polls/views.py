from django.shortcuts import render
from django.http import Http404  
from django.http import HttpResponseNotFound 
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, redirect
import operator
from django.urls import reverse
from .forms import questionForm, choiceForm
from datetime import datetime  
from django.contrib import messages 
from django.contrib.auth.decorators import user_passes_test

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def first(request, question_id):

	esc = Choice.objects.all().filter(question=question_id)
	ordered = sorted(esc, key=operator.attrgetter('votes'), reverse = True)
	first = ordered[0]
	return HttpResponse(first)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
	})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@user_passes_test(lambda u: u.is_superuser)
def newquestion(request):
        
	if request.method == "POST":
		form = questionForm(request.POST)
		if form.is_valid():
			question = form.save(commit=False)
			question.pub_date = datetime.now()
			question.save()
			messages.success(request, 'The question was save with success!')
	else:
		form = questionForm()

	return render(request, 'polls/formulario.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def newchoice(request):
        
	if request.method == "POST":
		form = choiceForm(request.POST)
		if form.is_valid():
			choice = form.save(commit=False)
			choice.save()
			messages.success(request, 'The option was save with success!')
	else:
		form = choiceForm()

	return render(request, 'polls/formulario.html', {'form': form})

def list(request):
	question = Question.objects.all()

	print(Question)
	return render(request, 'polls/listquestions.html', {'questions': question})

@user_passes_test(lambda u: u.is_superuser)
def editquestion(request, pk):
	question = get_object_or_404(Question, pk=pk)
	if request.method == "POST":
		form = questionForm(request.POST, instance=question)
		if form.is_valid():
			question = form.save(commit=False)
			question.save()
			messages.success(request, 'The question was edit with success!')
			return redirect('polls:list')
	else:
		form = questionForm(instance=question)
	return render(request, 'polls/formulario.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def deletequestion(request,pk):
	question = get_object_or_404(Question, pk=pk)
	question.delete()
	messages.success(request, 'The question was delete with success!')
	return redirect('polls:list')


def listchoices(request):
	choices = Choice.objects.all()
	return render(request, 'polls/listchoices.html', {'choices': choices})

@user_passes_test(lambda u: u.is_superuser)
def editchoice(request, pk):
	choice = get_object_or_404(Choice, pk=pk)
	if request.method == "POST":
		form = choiceForm(request.POST, instance=choice)
		if form.is_valid():
			choice = form.save(commit=False)
			choice.save()
			messages.success(request, 'The option was edit with success!')
			return redirect('polls:listchoices')
	else:
		form = choiceForm(instance=choice)
	return render(request, 'polls/formulario.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def deletechoice(request,pk):
	choice = get_object_or_404(Choice, pk=pk)
	choice.delete()
	messages.success(request, 'The option was delete with success!')
	return redirect('polls:listchoices')