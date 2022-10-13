from django.db import models
from users.models import User

CATEGORY_CHOICES = (
    ('teachers','Mugallymlar we okuwçylar'),
    ('students', 'Içerki daşarky Talyplar'),
    ('masters','Ussatlar'),
    ('internet', 'Internet'),
    ('jokes', 'Degişmeler')
)

# Create your models here.
class Content(models.Model):
	image_1 = models.ImageField(upload_to = 'images')
	image_2 = models.ImageField(upload_to = 'images')
	image_3 = models.ImageField(upload_to = 'images')
	body = models.TextField()
	link = models.URLField()
	category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body

class Comment_for_Content(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.ForeignKey(Content, on_delete = models.CASCADE, related_name = 'comments')
	reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
