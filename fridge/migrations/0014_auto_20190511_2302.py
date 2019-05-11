# Generated by Django 2.2.1 on 2019-05-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0013_auto_20190511_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.CharField(choices=[('2019', '2019년'), ('2020', '2020년'), ('2021', '2021년'), ('2022', '2022년'), ('2023', '2023년')], default='2019', max_length=200),
        ),
    ]
