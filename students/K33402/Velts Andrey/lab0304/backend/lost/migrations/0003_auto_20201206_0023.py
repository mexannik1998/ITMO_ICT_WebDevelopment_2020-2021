# Generated by Django 3.1.4 on 2020-12-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0002_auto_20201205_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='gender',
            field=models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], default='Мальчик', max_length=14, verbose_name='Пол'),
        ),
    ]
