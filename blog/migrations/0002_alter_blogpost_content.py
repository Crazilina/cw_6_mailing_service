# Generated by Django 5.0.6 on 2024-06-17 07:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержимое статьи'),
        ),
    ]