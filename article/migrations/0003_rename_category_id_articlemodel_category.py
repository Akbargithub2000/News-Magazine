# Generated by Django 4.1.1 on 2023-10-01 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_articlemodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlemodel',
            old_name='category_id',
            new_name='category',
        ),
    ]