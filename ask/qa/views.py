from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question_view(request, q_id):
	try:
		question = Question.objects.get(id = q_id)
	except Question.DoesNotExist:
		raise Http404
	return render(request, 'question.html', {
		'question': question,
		'title': question.title,
		'text': question.text,
		})

def popular_view(request):
	return HttpResponse('OK')
		
