# Generated by Django 3.1.7 on 2023-11-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0004_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='comment',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
