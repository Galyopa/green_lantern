# Generated by Django 3.0.6 on 2020-06-18 16:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_auto_20200605_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='photos/')),
                ('position', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='cars.Car')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]