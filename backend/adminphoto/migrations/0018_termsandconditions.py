# Generated by Django 4.0.3 on 2023-04-08 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminphoto', '0017_contact_description_contact_short_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms', models.TextField(blank=True, max_length=200000, null=True)),
            ],
        ),
    ]
