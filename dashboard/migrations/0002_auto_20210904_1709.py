# Generated by Django 3.2.7 on 2021-09-04 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='discription',
            new_name='description',
        ),
    ]
