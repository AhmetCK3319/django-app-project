# Generated by Django 4.1.7 on 2023-04-06 03:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descriptions',
            field=ckeditor.fields.RichTextField(),
        ),
    ]