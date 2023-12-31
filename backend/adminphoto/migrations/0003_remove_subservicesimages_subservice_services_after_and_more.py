# Generated by Django 4.0.3 on 2023-04-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminphoto', '0002_subservices_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subservicesimages',
            name='subservice',
        ),
        migrations.AddField(
            model_name='services',
            name='after',
            field=models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='services',
            name='before',
            field=models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subservices',
            name='after',
            field=models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='subservices',
            name='before',
            field=models.ImageField(blank=True, default='image-placeholder-500x500.jpg', null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='ServicesImages',
        ),
        migrations.DeleteModel(
            name='SubServicesImages',
        ),
    ]
