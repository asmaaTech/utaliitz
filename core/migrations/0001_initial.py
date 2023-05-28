# Generated by Django 4.2.1 on 2023-05-23 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='attractions/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TourOperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='touroperators/')),
                ('email', models.EmailField(max_length=254)),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touroperators', to='core.attraction')),
            ],
        ),
        migrations.CreateModel(
            name='InterestingFacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facts', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='facts/')),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interestingfacts', to='core.attraction')),
            ],
            options={
                'verbose_name_plural': 'Interesting Facts',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hotels/')),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='core.attraction')),
            ],
        ),
        migrations.AddField(
            model_name='attraction',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to='core.location'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to='core.type'),
        ),
    ]
