# Generated by Django 3.1.3 on 2020-11-17 05:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product_code', models.IntegerField(unique=True)),
                ('product_name', models.CharField(max_length=150)),
                ('product_price', models.CharField(max_length=20)),
                ('product_desciption', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
