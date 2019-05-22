# Generated by Django 2.2.1 on 2019-05-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190519_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='imagePath',
            new_name='imagepath',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='resume_education',
            old_name='imagePath',
            new_name='imagepath',
        ),
        migrations.RenameField(
            model_name='resume_education',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='resume_experience',
            old_name='imagePath',
            new_name='imagepath',
        ),
        migrations.RenameField(
            model_name='resume_experience',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='imagePath',
            new_name='displayname',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='skill',
            name='imagepath',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume_education',
            name='start',
            field=models.DateTimeField(blank=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='resume_experience',
            name='start',
            field=models.DateTimeField(blank=True, verbose_name='Start Date'),
        ),
    ]