# Generated by Django 3.1.7 on 2021-08-10 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PATH', '0005_auto_20210810_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_book',
            name='pump',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PATH.pumpdetail'),
        ),
    ]