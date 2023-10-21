# Generated by Django 4.2.6 on 2023-10-21 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='places/')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='property/')),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_category', to='preporty.category', verbose_name='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_place', to='preporty.place', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('feedback', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_property', to='preporty.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='propertyimages/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Property_image', to='preporty.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=django.utils.timezone.now)),
                ('date_to', models.DateField(default=django.utils.timezone.now)),
                ('guest', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2)),
                ('children', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_property', to='preporty.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]