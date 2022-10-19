# Generated by Django 3.2.16 on 2022-10-18 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link1', models.URLField(blank=True)),
                ('link2', models.URLField(blank=True)),
                ('link3', models.URLField(blank=True)),
                ('word1', models.CharField(blank=True, max_length=30)),
                ('word2', models.CharField(blank=True, max_length=30)),
                ('word3', models.CharField(blank=True, max_length=30)),
                ('category', models.CharField(choices=[('english', 'Inlis Dili'), ('russian', 'Rus Dili'), ('chinese', 'Hytay dili'), ('turkish', 'Turk dili')], max_length=30)),
                ('language', models.CharField(choices=[('english', 'Inlis Dili'), ('russian', 'Rus Dili'), ('chinese', 'Hytay dili'), ('turkish', 'Turk dili'), ('turkmen', 'Turkmen Dili')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setting.lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
