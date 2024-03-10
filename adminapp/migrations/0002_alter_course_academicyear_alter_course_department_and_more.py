# Generated by Django 5.0 on 2024-01-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='academicyear',
            field=models.CharField(choices=[('2023-24', '2023-24'), ('2022-23', '2022-23'), ('2021-22', '2021-22')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('CSE(Regular)', 'CSE(R)'), ('CSE(Honors)', 'CSE(H)'), ('CSE&IT', 'CSEIT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=20),
        ),
    ]
