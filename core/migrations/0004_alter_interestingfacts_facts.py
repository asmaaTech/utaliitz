# Generated by Django 4.2.1 on 2023-05-25 13:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_attraction_content_hotel_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestingfacts',
            name='facts',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
