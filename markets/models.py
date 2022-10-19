from django.db import models
ETRAP_CHOICES = (
    ('yaslyk','Ýaşlyk'),('akbugday','Ak bugdaý'),('baherden','Bäherden'),
    ('babadayhan','Babadaýhan'),('gokdepe','Gökdepe'),('kaka','Kaka'),
    ('anew','Änew'),('tejen','Tejen'),('sarahs','Sarahs'),
    ('magtymguly','Magtymguly'),('bereket','Bereket'),('etrek','Etrek'),
    ('esenguly','Esenguly'),('gumdag','Gumdag'),('garabogaz','Garabogaz'),
    ('balkanabat','Balkanabat'),('hazar','Hazar'),('serdar','Serdar'),
    ('turkmenbasy','Türkmenbaşy'),('jebel','Jebel'),('yoloten','Ýolöten'),
    ('mary','Mary'),('murgap','Murgap'),('sakarcage','Sakarçäge'),
    ('serhetabat','Serhetabat'),('tagtabazar','Tagtabazar'),('turkmengala','Türkmengala'),
    ('oguzhan','Oguz han'),('satlyk','Şatlyk'),('bayramaly','Baýramaly'),
    ('wekilbazar','Wekilbazar'),('garagum','Garagum'),('darganata','Darganata'),
    ('farap','Farap'),('gazojak','Gazojak'),('danew','Dänew'),
    ('garabekewul','Garabekewül'),('turkmenabat','Türkmenabat'),('dostluk','Dostluk'),
    ('hojambaz','Hojambaz'),('koytendag','Köýtendag'),('magdanly','Magdanly'),
    ('kerki','Kerki'),('sakar','Sakar'),('sayat','Saýat'),('seydi','Seýdi'),
    ('carjew','Çärjew'),('halac','Halaç'),('akdepe','Akdepe'),('gurbansoltaneje','Gurbansoltan Eje'),
    ('boldumsaz','Boldumsaz'),('gubadag','Gubadag'),('dasoguz','Daşoguz'),('gorogly','Görogly'),
    ('turkmenbasy','Türkmenbaşy'),  ('ruhubelent','Ruhubelent'),('koneurgenc','Köneürgenç'),('sanyyazow','S.A. Nyýazow'),
)

REG_CHOICES = (
    ('default',"Ulanyjy"),
    ("market","Market"),
    ("service", 'Hyzmat'),
)

class Category(models.Model):
    name = models.CharField(max_length=200)
    un = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Kategoriya")
        verbose_name_plural = ("Kategoriyalar")

    def __str__(self):
        return self.name
# Create your models here.

class Market(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, primary_key = True)
    image_1 = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to = 'images')
    region = models.CharField(max_length=50, choices = ETRAP_CHOICES)
    reg = models.CharField(max_length=50, choices = REG_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=400)
    warning = models.TextField()
    place = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    about = models.TextField()

    class Meta:
        verbose_name = ("Market")
        verbose_name_plural = ("Marketler")

    def __str__(self):
        return self.name

class Product(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name = 'products')

    name = models.CharField(max_length=400)
    price = models.CharField(max_length=200)
    about = models.TextField()
    image_1 = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to='images')
    image_3 = models.ImageField(upload_to='images')    
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("Haryt")
        verbose_name_plural = ("Harytlar")

    def __str__(self):
        return self.name
