# Generated by Django 4.0.4 on 2024-03-27 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_remove_contact_phone_1_remove_contact_phone_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='mobile',
            field=models.CharField(default=0, max_length=12),
        ),
    ]
