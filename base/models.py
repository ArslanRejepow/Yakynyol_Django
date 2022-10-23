from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Left_Ad(models.Model):
	image = models.ImageField(upload_to='images', verbose_name = 'Surat')
	link = models.URLField(verbose_name = 'link')
	
	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	def __str__(self):
		return self.link
	
	class Meta:
		verbose_name = ('Sag reklama')
		verbose_name_plural = ('Sag Reklamalar')

	def serialize(self):
		return {
            "image": self.image.url,
            "link": self.link 
        }