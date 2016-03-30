from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length = 50)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name = 'question_author')
	likes = models.ManyToManyField(User)
	class Meta:
		db_table = 'question'

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('question', kwargs={'id': self.id})

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, related_name = 'answer_author')
	class Meta:
		db_table = 'answer'

	def __unicode__(self):
		return self.author + self.added_at + self.text
			
