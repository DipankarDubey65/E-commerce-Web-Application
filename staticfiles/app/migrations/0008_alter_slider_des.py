# Generated by Django 3.2.4 on 2024-07-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='des',
            field=models.TextField(),
        ),
    ]
