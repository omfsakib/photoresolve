# Generated by Django 4.0.3 on 2023-04-06 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminphoto', '0005_portfolio_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='src',
        ),
    ]