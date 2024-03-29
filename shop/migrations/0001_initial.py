# Generated by Django 3.0.5 on 2020-05-14 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='shops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterprise_type', models.CharField(default='ፋብሪካ', max_length=100, null=True)),
                ('name', models.CharField(max_length=300)),
                ('detail_text', models.TextField(max_length=1000, null=True, verbose_name='Detail Text')),
                ('location1', models.CharField(max_length=100, null=True)),
                ('location2', models.CharField(max_length=100, null=True)),
                ('location3', models.CharField(default='ባህር ዳር', max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('TIN_number', models.CharField(max_length=30)),
                ('mainimage', models.ImageField(blank=True, upload_to='gallery/TIN')),
                ('approved', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
