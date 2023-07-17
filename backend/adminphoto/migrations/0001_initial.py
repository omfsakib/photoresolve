# Generated by Django 4.0.3 on 2023-04-06 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('rate', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('rate', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubServicesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before', models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to='')),
                ('after', models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to='')),
                ('subservice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminphoto.subservices')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before', models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to='')),
                ('after', models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to='')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminphoto.services')),
            ],
        ),
    ]
