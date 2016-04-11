from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import Http404
from django.template.loader import get_template
from django.template import Context
from qa.models import Question, Answer
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
		'paginator': paginator,
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
	question = Question.objects.get(id=q_id)

	return render_to_response('question.html', {
		'title': "question",
		'question': Question.objects.get(id=q_id),
		'answers': question.answer_set.all(),
		})
	#return HttpResponse('OK')
		
