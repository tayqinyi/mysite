# Generated by Django 2.2.1 on 2019-05-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('imagePath', models.TextField(blank=True)),
                ('classes', models.TextField(blank=True)),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(blank=True, verbose_name='End Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume_Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('imagePath', models.TextField(blank=True)),
                ('classes', models.TextField(blank=True)),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(blank=True, verbose_name='End Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('imagePath', models.TextField(blank=True)),
                ('classes', models.TextField(blank=True)),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(blank=True, verbose_name='End Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('imagePath', models.TextField(blank=True)),
                ('classes', models.TextField(blank=True)),
                ('level', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
