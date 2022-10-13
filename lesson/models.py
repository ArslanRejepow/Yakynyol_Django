from django.db import models
from setting.models import Lesson
from users.models import User

class Word(models.Model):
	another_lang = models.CharField(max_length = 100)
	turkmen = models.CharField(max_length = 100)
	additional1 = models.TextField(blank = True)
	additional2 = models.TextField(blank = True)
	additional3 = models.TextField(blank = True)
	description = models.TextField(blank = True)
	audio_another = models.FileField(upload_to = 'words')
	audio_turkmen = models.FileField(upload_to = 'words')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)

	def __str__(self):
		return self.another_lang + " - " + self.turkmen
# Create your models here.

class Dialog(models.Model):
	question_another = models.TextField()
	answer_another = models.TextField()
	question_turkmen = models.TextField()
	answer_turkmen = models.TextField()
	description = models.TextField(blank = True)
	additional1 = models.TextField(blank = True)
	additional2 = models.TextField(blank = True)
	wrong_text = models.TextField(blank = True)
	audio_question_another = models.FileField(upload_to = 'words')
	audio_answer_another = models.FileField(upload_to = 'words')
	audio_question_turkmen = models.FileField(upload_to = 'words')
	audio_answer_turkmen = models.FileField(upload_to = 'words')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)

	def __str__(self):
		return self.question_another + " - " + self.question_turkmen


class Text(models.Model):
	another_lang = models.TextField()
	turkmen = models.TextField()
	audio_another = models.FileField(upload_to = 'words')
	audio_turkmen = models.FileField(upload_to = 'words')
	image_another = models.ImageField(upload_to = 'images')
	image_turkmen = models.ImageField(upload_to = 'images')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)

	def __str__(self):
		return self.another_lang + " - " + self.turkmen

class Comment(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name = 'comments')
	reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')




