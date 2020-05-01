# Generated by Django 2.2.4 on 2019-11-21 10:36

import ckeditor_uploader.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('img', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=75, size=[480, 320], upload_to='')),
                ('logo', models.ImageField(upload_to='')),
                ('trade', models.CharField(max_length=100)),
                ('goal', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('opinion', models.CharField(max_length=200)),
                ('opinion_owner', models.CharField(max_length=100)),
                ('opinion_owner_position', models.CharField(max_length=100)),
            ],
        ),
    ]
