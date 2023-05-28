# Generated by Django 4.2.1 on 2023-05-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_attractionfee'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractionfee',
            name='currency',
            field=models.CharField(choices=[('USD', 'Usd'), ('TZS', 'Tzs')], max_length=20, null=True),
        ),
    ]