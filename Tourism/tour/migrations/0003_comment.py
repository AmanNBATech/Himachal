# Generated by Django 4.1.7 on 2023-07-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_rename_image_trek_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
            ],
        ),
    ]
