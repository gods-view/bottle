# Generated by Django 2.0.1 on 2018-05-27 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_products_imgurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='imgurl',
        ),
    ]
