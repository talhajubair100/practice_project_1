# Generated by Django 3.0.8 on 2020-07-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='area',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='district',
            name='intro',
            field=models.TextField(),
        ),
    ]
