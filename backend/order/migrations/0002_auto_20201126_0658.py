# Generated by Django 3.1.3 on 2020-11-26 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authtoken.token'),
        ),
    ]
