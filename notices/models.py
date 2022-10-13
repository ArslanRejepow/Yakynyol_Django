from django.db import models
from users.models import User

CATEGORY_CHOICES = (
    ('onumchilik','Önümçilik'),
    ('sowda', 'Söwda'),
    ('okuw','Okuw'),
    ('habar', 'Habar')
)

# Create your models here.
class Notice(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	body = models.TextField()
	image = models.ImageField(upload_to = 'images')
	link = models.URLField()
	category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES)
	date = models.DateTimeField(auto_now_add = True)
	isComment = models.BooleanField(default = True)
	is_active = models.BooleanField(default = False)
	