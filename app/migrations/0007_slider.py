# Generated by Django 3.2.4 on 2024-07-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_recommeditems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ecommerce/pimg')),
                ('title', models.CharField(max_length=50)),
                ('hading', models.CharField(max_length=100)),
                ('des', models.CharField(max_length=500)),
            ],
        ),
    ]
