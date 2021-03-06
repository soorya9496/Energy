# Generated by Django 3.1.7 on 2021-08-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PATH', '0012_auto_20210811_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_oilbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('oiladdress', models.CharField(max_length=50, null=True)),
                ('oil_c_address', models.CharField(max_length=50, null=True)),
                ('oilplace', models.CharField(max_length=50, null=True)),
                ('oilphone', models.IntegerField(null=True)),
                ('oilfuel', models.CharField(max_length=10, null=True)),
                ('oilquantity', models.IntegerField(null=True)),
                ('oilpump', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
