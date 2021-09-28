# Generated by Django 3.2.7 on 2021-09-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('author', models.CharField(max_length=10, verbose_name='Автор')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
