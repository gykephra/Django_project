# Generated by Django 4.0.4 on 2022-12-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnes', '0004_personnes_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objets',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='objet'),
        ),
        migrations.AlterField(
            model_name='personnes',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='personne'),
        ),
    ]
