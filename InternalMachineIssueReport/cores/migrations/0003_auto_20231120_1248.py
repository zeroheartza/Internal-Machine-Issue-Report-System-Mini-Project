# Generated by Django 3.1.7 on 2023-11-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0002_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue',
            field=models.CharField(max_length=150),
        ),
    ]
