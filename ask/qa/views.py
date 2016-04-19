from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template.loader import get_template
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def main_view(request):
	page_number = request.GET.get('page', 1)
	questions = Question.objects.order_by('-added_at')
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/?page='
	page = paginator.page(page_number)
	return render(request, 'questions.html', {
		'title': "Main",
		'questions': page.object_list,
		#'paginator': paginator,
		'page': page,
	})
	

def popular_view(request):
	page_number = request.GET.get('page', 1)
	questions = Question.objects.order_by('-rating')
	paginator = Paginator(questions, 10)
	paginator.baseurl = '/popular/?page='
	page = paginator.page(page_number)

	return render(request, 'questions.html', {
		'title': "Popular",
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		})

def question_view(request, q_id):
	if request.method is 'POST':
		return answer_add(request)
	question_obj = Question.objects.get(id=q_id)
	form = AnswerForm(initial={'question': q_id})
	return render(request, 'question.html', {
		'title': "question",
		'question': Question.objects.get(id=q_id),
		'answers': question_obj.answer_set.all(),
		'form': form,
		})

def question_add(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			post = form.save()
			url = post.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'question_add.html', {
		'form': form,
	})

def answer_add(request):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			answer = form.save()
			url = answer.get_url()
			return HttpResponseRedirect(url)
	#else:
		#return main_view(request)
