from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length = 50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name = 'questAsAuthor')
	likes = models.ManyToManyField(User)
	class Meta:
		db_table = 'question'

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	class Meta:
		db_table = 'answer'
