# Generated by Django 3.0.5 on 2020-05-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asebeza', '0007_auto_20200530_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asebeza',
            name='mainimage',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='gallery/products'),
        ),
    ]
