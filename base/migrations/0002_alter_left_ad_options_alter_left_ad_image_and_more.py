# Generated by Django 4.1.3 on 2022-11-18 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='left_ad',
            options={'verbose_name': 'Sag reklama', 'verbose_name_plural': 'Sag Reklamalar'},
        ),
        migrations.AlterField(
            model_name='left_ad',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Surat'),
        ),
        migrations.AlterField(
            model_name='left_ad',
            name='link',
            field=models.URLField(verbose_name='link'),
        ),
    ]
