# Generated by Django 3.2.7 on 2022-01-22 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='userprojectcompleted',
            options={'verbose_name': 'Пользователь выполнивший проект', 'verbose_name_plural': 'Пользователи выполнившие проект'},
        ),
        migrations.AddField(
            model_name='project',
            name='id_telegram',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]