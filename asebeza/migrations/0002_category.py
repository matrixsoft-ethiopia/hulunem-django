# Generated by Django 3.0.5 on 2020-05-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asebeza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
