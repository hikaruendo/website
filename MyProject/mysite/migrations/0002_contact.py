# Generated by Django 2.1.2 on 2018-10-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=180)),
                ('message', models.TextField()),
            ],
        ),
    ]
