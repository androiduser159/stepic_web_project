from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	
	def clean(self):
		title = self.cleaned_data['title']
		text = self.cleaned_data['text']
		return self.cleaned_data

	def save(self):
		question = Question(**self.cleaned_data)
		question.author_id = 1
		question.save()
		return question
	
class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())

	def clean(self):
		#print self.cleaned_data
		text = self.cleaned_data['text']
		question = self.cleaned_data['question']
		return self.cleaned_data

	def save(self):
		#print self.cleaned_data['question']
		self.cleaned_data['question'] = Question.objects.get(id=self.cleaned_data['question'])
		#print self.cleaned_data
		answer = Answer(**self.cleaned_data)
		answer.author_id = 1
		answer.save()
		return answer
