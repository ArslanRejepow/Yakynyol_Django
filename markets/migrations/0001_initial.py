# Generated by Django 3.2.16 on 2022-10-19 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('un', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
                ('image_1', models.ImageField(upload_to='images')),
                ('image_2', models.ImageField(upload_to='images')),
                ('region', models.CharField(choices=[('yaslyk', 'Ýaşlyk'), ('akbugday', 'Ak bugdaý'), ('baherden', 'Bäherden'), ('babadayhan', 'Babadaýhan'), ('gokdepe', 'Gökdepe'), ('kaka', 'Kaka'), ('anew', 'Änew'), ('tejen', 'Tejen'), ('sarahs', 'Sarahs'), ('magtymguly', 'Magtymguly'), ('bereket', 'Bereket'), ('etrek', 'Etrek'), ('esenguly', 'Esenguly'), ('gumdag', 'Gumdag'), ('garabogaz', 'Garabogaz'), ('balkanabat', 'Balkanabat'), ('hazar', 'Hazar'), ('serdar', 'Serdar'), ('turkmenbasy', 'Türkmenbaşy'), ('jebel', 'Jebel'), ('yoloten', 'Ýolöten'), ('mary', 'Mary'), ('murgap', 'Murgap'), ('sakarcage', 'Sakarçäge'), ('serhetabat', 'Serhetabat'), ('tagtabazar', 'Tagtabazar'), ('turkmengala', 'Türkmengala'), ('oguzhan', 'Oguz han'), ('satlyk', 'Şatlyk'), ('bayramaly', 'Baýramaly'), ('wekilbazar', 'Wekilbazar'), ('garagum', 'Garagum'), ('darganata', 'Darganata'), ('farap', 'Farap'), ('gazojak', 'Gazojak'), ('danew', 'Dänew'), ('garabekewul', 'Garabekewül'), ('turkmenabat', 'Türkmenabat'), ('dostluk', 'Dostluk'), ('hojambaz', 'Hojambaz'), ('koytendag', 'Köýtendag'), ('magdanly', 'Magdanly'), ('kerki', 'Kerki'), ('sakar', 'Sakar'), ('sayat', 'Saýat'), ('seydi', 'Seýdi'), ('carjew', 'Çärjew'), ('halac', 'Halaç'), ('akdepe', 'Akdepe'), ('gurbansoltaneje', 'Gurbansoltan Eje'), ('boldumsaz', 'Boldumsaz'), ('gubadag', 'Gubadag'), ('dasoguz', 'Daşoguz'), ('gorogly', 'Görogly'), ('turkmenbasy', 'Türkmenbaşy'), ('ruhubelent', 'Ruhubelent'), ('koneurgenc', 'Köneürgenç'), ('sanyyazow', 'S.A. Nyýazow')], max_length=50)),
                ('reg', models.CharField(choices=[('default', 'Ulanyjy'), ('market', 'Market'), ('service', 'Hyzmat')], max_length=50)),
                ('code', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=400)),
                ('warning', models.TextField()),
                ('place', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('about', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.category')),
            ],
            options={
                'verbose_name': 'Market',
                'verbose_name_plural': 'Marketler',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('price', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('image_1', models.ImageField(upload_to='images')),
                ('image_2', models.ImageField(upload_to='images')),
                ('image_3', models.ImageField(upload_to='images')),
                ('date', models.DateField(auto_now=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='markets.market')),
            ],
            options={
                'verbose_name': 'Haryt',
                'verbose_name_plural': 'Harytlar',
            },
        ),
    ]
