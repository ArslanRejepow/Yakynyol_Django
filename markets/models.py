from django.db import models
from django.utils.html import mark_safe
ETRAP_CHOICES = (
    ('yaslyk', 'Ýaşlyk'), ('akbugday', 'Ak bugdaý'), ('baherden', 'Bäherden'),
    ('babadayhan', 'Babadaýhan'), ('gokdepe', 'Gökdepe'), ('kaka', 'Kaka'),
    ('anew', 'Änew'), ('tejen', 'Tejen'), ('sarahs', 'Sarahs'),
    ('magtymguly', 'Magtymguly'), ('bereket', 'Bereket'), ('etrek', 'Etrek'),
    ('esenguly', 'Esenguly'), ('gumdag', 'Gumdag'), ('garabogaz', 'Garabogaz'),
    ('balkanabat', 'Balkanabat'), ('hazar', 'Hazar'), ('serdar', 'Serdar'),
    ('turkmenbasy', 'Türkmenbaşy'), ('jebel', 'Jebel'), ('yoloten', 'Ýolöten'),
    ('mary', 'Mary'), ('murgap', 'Murgap'), ('sakarcage', 'Sakarçäge'),
    ('serhetabat', 'Serhetabat'), ('tagtabazar',
                                   'Tagtabazar'), ('turkmengala', 'Türkmengala'),
    ('oguzhan', 'Oguz han'), ('satlyk', 'Şatlyk'), ('bayramaly', 'Baýramaly'),
    ('wekilbazar', 'Wekilbazar'), ('garagum',
                                   'Garagum'), ('darganata', 'Darganata'),
    ('farap', 'Farap'), ('gazojak', 'Gazojak'), ('danew', 'Dänew'),
    ('garabekewul', 'Garabekewül'), ('turkmenabat',
                                     'Türkmenabat'), ('dostluk', 'Dostluk'),
    ('hojambaz', 'Hojambaz'), ('koytendag', 'Köýtendag'), ('magdanly', 'Magdanly'),
    ('kerki', 'Kerki'), ('sakar', 'Sakar'), ('sayat', 'Saýat'), ('seydi', 'Seýdi'),
    ('carjew', 'Çärjew'), ('halac', 'Halaç'), ('akdepe',
                                               'Akdepe'), ('gurbansoltaneje', 'Gurbansoltan Eje'),
    ('boldumsaz', 'Boldumsaz'), ('gubadag',
                                 'Gubadag'), ('dasoguz', 'Daşoguz'), ('gorogly', 'Görogly'),
    ('turkmenbasy', 'Türkmenbaşy'),  ('ruhubelent',
                                      'Ruhubelent'), ('koneurgenc', 'Köneürgenç'), ('sanyyazow', 'S.A. Nyýazow'),
)

REG_CHOICES = (
    ('default', "Ulanyjy"),
    ("market", "Market"),
    ("service", 'Hyzmat'),
)


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Ady')
    un = models.CharField(max_length=200, verbose_name='Id')

    class Meta:
        verbose_name = ("Kategoriya")
        verbose_name_plural = ("Kategoriyalar")

    def __str__(self):
        return self.name
# Create your models here.


class Market(models.Model):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, primary_key=True, verbose_name='Ulanyjy')
    image_1 = models.ImageField(upload_to='images', verbose_name='Surat 1')
    image_2 = models.ImageField(upload_to='images', verbose_name='Surat2')
    region = models.CharField(
        max_length=50, choices=ETRAP_CHOICES, verbose_name='Etraby')
    reg = models.CharField(max_length=50, choices=REG_CHOICES,
                           verbose_name='Registrasiya nomeri')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Kategoriya')
    code = models.CharField(max_length=100, verbose_name='Market Kody')
    phone_number = models.CharField(
        max_length=200, verbose_name='Telefon Nomeri')
    name = models.CharField(max_length=400, verbose_name='Ady')
    warning = models.TextField(verbose_name='Duýduryş tekksti')
    place = models.CharField(max_length=50, verbose_name='Ýeri')
    date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Senesi')
    about = models.TextField(verbose_name='Hakynda')

    def image_tag1(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_1.url))

    def image_tag2(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image_2.url))
    image_tag2.short_description = 'Surat 2'
    image_tag2.allow_tags = True

    image_tag1.short_description = 'Surat 1'
    image_tag1.allow_tags = True

    class Meta:
        verbose_name = ("Market")
        verbose_name_plural = ("Marketler")

    def __str__(self):
        return self.name


class Product(models.Model):
    market = models.ForeignKey(
        Market, on_delete=models.CASCADE, related_name='products', verbose_name='Market')

    name = models.CharField(max_length=400, verbose_name='Ady')
    price = models.CharField(max_length=200, verbose_name='Bahasy')
    about = models.TextField(verbose_name='Hakynda')
    image_1 = models.ImageField(upload_to='images', verbose_name='Surat 1')
    image_2 = models.ImageField(upload_to='images', verbose_name='Surat 2')
    image_3 = models.ImageField(upload_to='images', verbose_name='Surat 3')
    date = models.DateField(auto_now=True, verbose_name='Senesii')

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
        verbose_name = ("Haryt")
        verbose_name_plural = ("Harytlar")

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Service(models.Model):
    market = models.ForeignKey(
        Market, on_delete=models.CASCADE, related_name='services', verbose_name='Hyzmat')

    name = models.CharField(max_length=400, verbose_name='Ady')
    price = models.CharField(max_length=200, verbose_name='Bahasy')
    about = models.TextField(verbose_name='Hakynda')
    image = models.ImageField(upload_to='images', verbose_name='Surat 1')
    date = models.DateField(auto_now=True, verbose_name='Senesii')

    def image_tag1(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))

    image_tag1.short_description = 'Surat 1'
    image_tag1.allow_tags = True

    class Meta:
        verbose_name = ("Hyzmat")
        verbose_name_plural = ("Hyzmatlar")

    def __str__(self):
        return self.name


class ServiceFavourite(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
