# Generated by Django 4.1.2 on 2022-10-12 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=100)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
