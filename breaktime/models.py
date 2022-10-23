from django.db import models
from users.models import User
from django.utils.html import mark_safe

CATEGORY_CHOICES = (
    ('teachers','Mugallymlar we okuwçylar'),
    ('students', 'Içerki daşarky Talyplar'),
    ('masters','Ussatlar'),
    ('internet', 'Internet'),
    ('jokes', 'Degişmeler')
)

# Create your models here.
class Content(models.Model):
	image_1 = models.ImageField(upload_to = 'images', verbose_name = 'Surat 1')
	image_2 = models.ImageField(upload_to = 'images', verbose_name = 'Surat 2')
	image_3 = models.ImageField(upload_to = 'images', verbose_name = 'Surat 3')
	body = models.TextField(verbose_name = 'Teksti')
	link = models.URLField(verbose_name = 'Link')
	category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES, verbose_name = 'Kategoriýa')
	created_at = models.DateTimeField(auto_now=True, verbose_name = 'Wagty')
	def image_tag1(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_1.url))

	def image_tag2(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_2.url))

	def image_tag3(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_3.url))

	image_tag2.short_description = 'Surat 2'
	image_tag2.allow_tags = True

	image_tag1.short_description = 'Surat 1'
	image_tag1.allow_tags = True

	image_tag3.short_description = 'Surat3'
	image_tag3.allow_tags = True
	class Meta:
		verbose_name = ("Arakesme tekst")
		verbose_name_plural = ("Arakesme tekstler")

	def __str__(self):
		return self.body

class Comment_for_Content(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.ForeignKey(Content, on_delete = models.CASCADE, related_name = 'comments')
	reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

class Favorites_Content(models.Model):
	user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name = 'favorite_contents')
	content = models.ForeignKey(Content, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + "  --  " + self.content.body