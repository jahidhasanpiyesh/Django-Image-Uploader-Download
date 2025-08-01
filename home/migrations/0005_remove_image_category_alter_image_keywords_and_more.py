# Generated by Django 5.2.1 on 2025-07-02 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_image_caption_image_keywords_image_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AlterField(
            model_name='image',
            name='keywords',
            field=models.CharField(help_text='Comma‑separated keywords (e.g. computer,laptop)', max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='myimages/'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
