# Generated by Django 2.2.5 on 2019-09-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_auto_20190918_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]