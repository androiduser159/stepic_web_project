from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)
	
	def clean(self):
		#title = self.cleaned_data['title']
		#text = self.cleaned_data['text']
		self.cleaned_data = super(AskForm, self).clean()
		return self.cleaned_data

	def save(self):
		question = Question(**self.cleaned_data)
		self.cleaned_data['author'] = self._user	
		question.save()
		return question
	
class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput())

	def clean(self):
		#print self.cleaned_data
		#text = self.cleaned_data['text']
		#question = self.cleaned_data['question']
		self.cleaned_data = super(AnswerForm, self).clean()
		return self.cleaned_data

	def save(self):
		self.cleaned_data['question'] = Question.objects.get(id=self.cleaned_data['question'])
		self.cleaned_data['author'] = self._user	
		#print self.cleaned_data
		answer = Answer(**self.cleaned_data)
		answer.save()
		return answer

class UserForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.EmailField(widget=forms.EmailInput)
	password = forms.CharField(widget=forms.PasswordInput())

	def clean(self):
		self.cleaned_data = super(UserForm, self).clean()
		return self.cleaned_data

	def save(self):
		user = User.objects.create_user(**self.cleaned_data)
		user.save()
		return user
