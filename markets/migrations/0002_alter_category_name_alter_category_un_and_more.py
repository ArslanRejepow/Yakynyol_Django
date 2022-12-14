# Generated by Django 4.1.3 on 2022-11-18 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Ady'),
        ),
        migrations.AlterField(
            model_name='category',
            name='un',
            field=models.CharField(max_length=200, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='market',
            name='about',
            field=models.TextField(verbose_name='Hakynda'),
        ),
        migrations.AlterField(
            model_name='market',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.category', verbose_name='Kategoriya'),
        ),
        migrations.AlterField(
            model_name='market',
            name='code',
            field=models.CharField(max_length=100, verbose_name='Market Kody'),
        ),
        migrations.AlterField(
            model_name='market',
            name='date',
            field=models.DateField(verbose_name='Senesi'),
        ),
        migrations.AlterField(
            model_name='market',
            name='image_1',
            field=models.ImageField(upload_to='images', verbose_name='Surat 1'),
        ),
        migrations.AlterField(
            model_name='market',
            name='image_2',
            field=models.ImageField(upload_to='images', verbose_name='Surat2'),
        ),
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=400, verbose_name='Ady'),
        ),
        migrations.AlterField(
            model_name='market',
            name='phone_number',
            field=models.CharField(max_length=200, verbose_name='Telefon Nomeri'),
        ),
        migrations.AlterField(
            model_name='market',
            name='place',
            field=models.CharField(max_length=50, verbose_name='??eri'),
        ),
        migrations.AlterField(
            model_name='market',
            name='reg',
            field=models.CharField(choices=[('default', 'Ulanyjy'), ('market', 'Market'), ('service', 'Hyzmat')], max_length=50, verbose_name='Registrasiya nomeri'),
        ),
        migrations.AlterField(
            model_name='market',
            name='region',
            field=models.CharField(choices=[('yaslyk', '??a??lyk'), ('akbugday', 'Ak bugda??'), ('baherden', 'B??herden'), ('babadayhan', 'Babada??han'), ('gokdepe', 'G??kdepe'), ('kaka', 'Kaka'), ('anew', '??new'), ('tejen', 'Tejen'), ('sarahs', 'Sarahs'), ('magtymguly', 'Magtymguly'), ('bereket', 'Bereket'), ('etrek', 'Etrek'), ('esenguly', 'Esenguly'), ('gumdag', 'Gumdag'), ('garabogaz', 'Garabogaz'), ('balkanabat', 'Balkanabat'), ('hazar', 'Hazar'), ('serdar', 'Serdar'), ('turkmenbasy', 'T??rkmenba??y'), ('jebel', 'Jebel'), ('yoloten', '??ol??ten'), ('mary', 'Mary'), ('murgap', 'Murgap'), ('sakarcage', 'Sakar????ge'), ('serhetabat', 'Serhetabat'), ('tagtabazar', 'Tagtabazar'), ('turkmengala', 'T??rkmengala'), ('oguzhan', 'Oguz han'), ('satlyk', '??atlyk'), ('bayramaly', 'Ba??ramaly'), ('wekilbazar', 'Wekilbazar'), ('garagum', 'Garagum'), ('darganata', 'Darganata'), ('farap', 'Farap'), ('gazojak', 'Gazojak'), ('danew', 'D??new'), ('garabekewul', 'Garabekew??l'), ('turkmenabat', 'T??rkmenabat'), ('dostluk', 'Dostluk'), ('hojambaz', 'Hojambaz'), ('koytendag', 'K????tendag'), ('magdanly', 'Magdanly'), ('kerki', 'Kerki'), ('sakar', 'Sakar'), ('sayat', 'Sa??at'), ('seydi', 'Se??di'), ('carjew', '????rjew'), ('halac', 'Hala??'), ('akdepe', 'Akdepe'), ('gurbansoltaneje', 'Gurbansoltan Eje'), ('boldumsaz', 'Boldumsaz'), ('gubadag', 'Gubadag'), ('dasoguz', 'Da??oguz'), ('gorogly', 'G??rogly'), ('turkmenbasy', 'T??rkmenba??y'), ('ruhubelent', 'Ruhubelent'), ('koneurgenc', 'K??ne??rgen??'), ('sanyyazow', 'S.A. Ny??azow')], max_length=50, verbose_name='Etraby'),
        ),
        migrations.AlterField(
            model_name='market',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Ulanyjy'),
        ),
        migrations.AlterField(
            model_name='market',
            name='warning',
            field=models.TextField(verbose_name='Du??dury?? tekksti'),
        ),
        migrations.AlterField(
            model_name='product',
            name='about',
            field=models.TextField(verbose_name='Hakynda'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Senesii'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(upload_to='images', verbose_name='Surat 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(upload_to='images', verbose_name='Surat 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(upload_to='images', verbose_name='Surat 3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='markets.market', verbose_name='Market'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=400, verbose_name='Ady'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=200, verbose_name='Bahasy'),
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
