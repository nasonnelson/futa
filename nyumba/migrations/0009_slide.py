# Generated by Django 3.1.2 on 2022-04-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nyumba', '0008_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picha', models.ImageField(upload_to='')),
            ],
        ),
    ]
