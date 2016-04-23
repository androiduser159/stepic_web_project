from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length = 50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, default=1, related_name = 'question_author')
	likes = models.ManyToManyField(User)
	class Meta:
		db_table = 'question'

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('question', kwargs={'q_id': self.id})

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, related_name = 'answer_author')
	class Meta:
		db_table = 'answer'

	def __unicode__(self):
		return self.text
			
	def get_url(self):
		return reverse('question', kwargs={'q_id': self.question.id})

#class User(models.Model):
#	username = models.CharField(max_length=30, unique=True)
#	email = models.EmailField()
#	password = models.CharField(max_length=100)
#
#	def __unicode__(self):
#		return self.username

#class Session(models.Model):
#	key = models.CharField(max_length=100, unique=True)
#	user = models.ForeignKey(User)
#	expires = models.DateTimeField()
