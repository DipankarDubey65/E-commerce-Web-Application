# Generated by Django 3.2.4 on 2024-07-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ecommerce/pimg')),
                ('date', models.DateField(auto_now_add=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
