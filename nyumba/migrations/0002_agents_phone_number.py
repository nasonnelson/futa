# Generated by Django 3.1.2 on 2022-04-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nyumba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agents',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
