# Generated by Django 3.0.5 on 2020-06-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asebeza', '0008_auto_20200530_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asebeza',
            name='mainimage',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='gallery/asebeza'),
        ),
    ]
