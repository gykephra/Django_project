# Generated by Django 4.1.1 on 2022-11-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='personnes',
            name='commentaire',
            field=models.TextField(null=True),
        ),
    ]
