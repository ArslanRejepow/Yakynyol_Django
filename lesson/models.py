from django.db import models
from setting.models import Lesson
from users.models import User
from django.utils.html import mark_safe

class Word(models.Model):
	another_lang = models.CharField(max_length = 100, verbose_name = 'Beýleki dil')
	turkmen = models.CharField(max_length = 100, verbose_name = 'Türkmençe')
	additional1 = models.TextField(blank = True, verbose_name = 'Goşmaça 1')
	additional2 = models.TextField(blank = True, verbose_name = 'Goşmaça 2')
	additional3 = models.TextField(blank = True, verbose_name = 'Goşmaça 3')
	description = models.TextField(blank = True, verbose_name = 'Düşündirlişi')
	audio_another = models.FileField(upload_to = 'words', verbose_name = 'Ses Beýleki dil')
	audio_turkmen = models.FileField(upload_to = 'words', verbose_name = 'Ses Türkmençe')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, verbose_name = 'Sapagy')
	class Meta:
		verbose_name = 'Söz'
		verbose_name_plural = 'Sözler'
	def __str__(self):
		return self.another_lang + " - " + self.turkmen
# Create your models here.

class Dialog(models.Model):
	question_another = models.TextField(verbose_name = 'Sorag Beýleki dil')
	answer_another = models.TextField(verbose_name = 'Jogap Beýleki dil')
	question_turkmen = models.TextField(verbose_name = 'Sorag Türkmençe')
	answer_turkmen = models.TextField(verbose_name = 'Jogap Türkmençe')
	description = models.TextField(blank = True, verbose_name = 'Düşündirilişi')
	additional1 = models.TextField(blank = True, verbose_name = 'Goşmaça 1')
	additional2 = models.TextField(blank = True, verbose_name = 'Goşmaça 2')
	wrong_text = models.TextField(blank = True, verbose_name = 'Ýalňyş tekst')
	audio_question_another = models.FileField(upload_to = 'words', verbose_name = 'Ses Sorag Beýleki dil')
	audio_answer_another = models.FileField(upload_to = 'words', verbose_name = 'Ses Jogap Beýleki dil')
	audio_question_turkmen = models.FileField(upload_to = 'words', verbose_name = 'Ses Sorag Türkmençe')
	audio_answer_turkmen = models.FileField(upload_to = 'words', verbose_name = 'Ses Jogap Türkmençe')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, verbose_name = 'Sapagy')

	class Meta:
		verbose_name = 'Geplesik'
		verbose_name_plural = 'Geplesikler'
	def __str__(self):
		return self.question_another + " - " + self.question_turkmen


class Text(models.Model):
	another_lang = models.TextField(verbose_name = 'Beýlekki dil')
	turkmen = models.TextField(verbose_name = 'Türkmençe')
	audio_another = models.FileField(upload_to = 'words', verbose_name = 'Ses Beýleki dil')
	audio_turkmen = models.FileField(upload_to = 'words', verbose_name = 'SES Türkmençe')
	image_another = models.ImageField(upload_to = 'images', verbose_name = 'Surat Beýleki')
	image_turkmen = models.ImageField(upload_to = 'images', verbose_name = 'Surat Türkmençe')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, verbose_name= 'Sapagy')
	def image_tag1(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_another.url))

	def image_tag2(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_turkmen.url))

	image_tag2.short_description = 'Surat 2'
	image_tag2.allow_tags = True

	image_tag1.short_description = 'Surat 1'
	image_tag1.allow_tags = True
	class Meta:
		verbose_name = 'Tekst'
		verbose_name_plural = 'Tekstler'
	def __str__(self):
		return self.another_lang + " - " + self.turkmen

class Comment(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, related_name = 'comments')
	reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')




