# Generated by Django 3.1.7 on 2021-08-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PATH', '0009_auto_20210811_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_book',
            name='pump',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='PumpDetail',
        ),
    ]
