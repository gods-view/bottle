# Generated by Django 2.0.1 on 2018-06-16 12:52

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_products_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Content',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(verbose_name='描述'),
        ),
    ]
