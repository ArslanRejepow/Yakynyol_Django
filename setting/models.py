from django.db import models

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
	name = models.CharField(max_length=50)
	link1 = models.URLField(blank = True)
	link2 = models.URLField(blank = True)
	link3 = models.URLField(blank = True)
	word1 = models.CharField(max_length = 30, blank = True)
	word2 = models.CharField(max_length = 30, blank = True)
	word3 = models.CharField(max_length = 30, blank = True)
	category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
	language = models.CharField(max_length = 30, choices = LANGUAGE_CHOICES)

	def __str__(self):
		return self.name