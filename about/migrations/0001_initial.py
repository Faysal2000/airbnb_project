# Generated by Django 4.2.6 on 2023-10-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_we_do', models.TextField(max_length=1000)),
                ('our_mission', models.TextField(max_length=1000)),
                ('our_goals', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='FQA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('descraption', models.TextField(max_length=1000)),
            ],
        ),
    ]
