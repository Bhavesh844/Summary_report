# Generated by Django 4.2.7 on 2024-08-12 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_upload_file_delete_upload_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_file',
            name='file',
            field=models.FileField(error_messages='Please upload valid file', upload_to='media/', validators=[django.core.validators.FileExtensionValidator(['csv', 'xlsx'])]),
        ),
    ]
