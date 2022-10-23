from django.db import models
from users.models import User
from django.utils.html import mark_safe

CATEGORY_CHOICES = (
    ('onumchilik','Önümçilik'),
    ('sowda', 'Söwda'),
    ('okuw','Okuw'),
    ('habar', 'Habar')
)

# Create your models here.
class Notice(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "notices", verbose_name = 'Ulanyjy')
	body = models.TextField(verbose_name = 'Teksti')
	image = models.ImageField(upload_to = 'images', verbose_name = 'Surat')
	link = models.URLField(verbose_name = 'Link')
	category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES, verbose_name = 'Kategoriýa')
	date = models.DateTimeField(auto_now_add = True, verbose_name = 'Wagty')
	isComment = models.BooleanField(default = True, verbose_name = 'Kommentariya yazyp bilsinlermi')
	is_active = models.BooleanField(default = False, verbose_name = 'Aktiw')
	class Meta:
		verbose_name = 'Bildiriş'
		verbose_name_plural = 'Bildirişler'
	def image_tag(self):
		return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

	image_tag.short_description = 'Surat 2'
	image_tag.allow_tags = True

	def __str__(self):
		return self.body
	

class Comment_for_Notice(models.Model):
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.ForeignKey(Notice, on_delete = models.CASCADE, related_name = 'comments')
	reply_to = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

class Favorites_Notice(models.Model):
	user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name = 'favorite_notices')
	notice = models.ForeignKey(Notice, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username + "  --  " + self.notice.body