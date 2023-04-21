# Generated by Django 4.2 on 2023-04-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=64, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='email является логином пользователя', max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Фамилия'),
        ),
    ]
