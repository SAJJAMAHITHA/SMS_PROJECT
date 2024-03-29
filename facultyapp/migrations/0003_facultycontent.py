# Generated by Django 5.0 on 2024-02-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_alter_coursecontent_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField()),
                ('ccode', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('contentimage', models.ImageField(upload_to='content_images/')),
            ],
        ),
    ]
