# Generated by Django 2.0.2 on 2018-03-01 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_input_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='results',
            new_name='name_to_save',
        ),
    ]
