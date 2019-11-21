# Generated by Django 2.2.5 on 2019-11-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_auto_20190921_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='representative',
            name='daily_FTD',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='representative',
            name='daily_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='representative',
            name='monthly_FTD',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='representative',
            name='monthly_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='representative',
            name='target',
            field=models.IntegerField(),
        ),
    ]
