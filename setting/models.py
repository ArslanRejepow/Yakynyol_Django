from django.db import models
from users.models import User

CATEGORY_CHOICES = (
    ('english','Inlis Dili'),
    ('russian', 'Rus Dili'),
    ('chinese','Hytay dili'),
    ('turkish', 'Turk dili'),
)
LANGUAGE_CHOICES = (
    ('english','Inlis Dili'),
    ('russian', 'Rus Dili'),
    ('chinese','Hytay dili'),
    ('turkish', 'Turk dili'),
    ('turkmen', 'Turkmen Dili')
)

# Create your models here.
class Lesson(models.Model):
	name = models.CharField(max_length=50, verbose_name= 'Ady')
	link1 = models.URLField(blank = True, verbose_name= 'Video link 1')
	link2 = models.URLField(blank = True, verbose_name= 'Video link 2')
	link3 = models.URLField(blank = True, verbose_name= 'Video link 3')
	word1 = models.CharField(max_length = 30, blank = True, verbose_name= 'Video söz 1')
	word2 = models.CharField(max_length = 30, blank = True, verbose_name= 'Video Söz 2')
	word3 = models.CharField(max_length = 30, blank = True, verbose_name= 'Video Söz 3')
	category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, verbose_name= 'Kategoriýasy')
	language = models.CharField(max_length = 30, choices = LANGUAGE_CHOICES, verbose_name= 'Esasy dili')
	class Meta:
		verbose_name = 'Sapak'
		verbose_name_plural = 'Sapaklar'
	def __str__(self):
		return self.name

class Favorites(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'favorites', verbose_name='Ulanyjy')
	lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, verbose_name='Sapagy')
	class Meta:
		verbose_name = 'Halanlarym'
		verbose_name_plural = 'Halanlarym' 

	def __str__(self):
		return self.user.username + "  --  " + self.lesson.name