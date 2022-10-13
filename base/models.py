from django.db import models

# Create your models here.
class Left_Ad(models.Model):
	image = models.ImageField(upload_to='images')
	link = models.URLField()

	def __str__(self):
		return self.link