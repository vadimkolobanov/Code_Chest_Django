# Generated by Django 3.2.7 on 2021-12-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id_telegramm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]