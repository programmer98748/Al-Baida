# Generated by Django 4.2.3 on 2023-12-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('detail', models.TextField()),
                ('client_description', models.TextField()),
                ('image', models.FileField(upload_to='images/project')),
                ('requirements', models.TextField()),
                ('website', models.URLField()),
                ('categories', models.ManyToManyField(to='website.category')),
            ],
        ),
    ]