# Generated by Django 3.1.1 on 2020-09-29 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200929_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcommant',
            old_name='commant',
            new_name='comment',
        ),
    ]
