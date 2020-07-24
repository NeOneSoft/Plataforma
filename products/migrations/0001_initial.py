# Generated by Django 3.0.8 on 2020-07-24 02:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, validators=[django.core.validators.MinLengthValidator(3)])),
                ('value', models.FloatField(validators=[django.core.validators.MaxValueValidator(99998.9), django.core.validators.MinValueValidator(1.0)])),
                ('discount_value', models.FloatField(null=True)),
                ('stock', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
