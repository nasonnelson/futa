# Generated by Django 3.1.2 on 2022-04-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nyumba', '0003_auto_20220404_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jina_kitu', models.CharField(max_length=200)),
                ('maelezo', models.CharField(max_length=1000000)),
                ('picha', models.ImageField(upload_to='')),
            ],
        ),
    ]