# Generated by Django 4.2 on 2023-04-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.TextField(blank=True, null=True),
        ),
    ]