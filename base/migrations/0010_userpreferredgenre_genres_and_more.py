# Generated by Django 4.2.8 on 2024-04-13 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0009_userpreferredgenre'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferredgenre',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='users_with_preference', to='base.genre'),
        ),
        migrations.AlterField(
            model_name='userpreferredgenre',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_genres', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='userpreferredgenre',
            unique_together={('user',)},
        ),
        migrations.RemoveField(
            model_name='userpreferredgenre',
            name='genre',
        ),
    ]