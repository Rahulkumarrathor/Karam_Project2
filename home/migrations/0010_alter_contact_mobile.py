# Generated by Django 5.0.4 on 2024-05-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_addjob_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(max_length=12),
        ),
    ]
