# Generated by Django 3.1.7 on 2021-08-10 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PATH', '0002_emplogin_empregistration_staffregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='PumpDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, null=True, unique=True)),
                ('lname', models.CharField(max_length=50, null=True, unique=True)),
                ('address', models.CharField(max_length=50, null=True, unique=True)),
                ('c_address', models.CharField(max_length=50, null=True, unique=True)),
                ('place', models.CharField(max_length=50, null=True, unique=True)),
                ('phone', models.IntegerField(null=True)),
                ('fuel', models.CharField(max_length=10, null=True, unique=True)),
                ('quantity', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=10)),
                ('pump', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='PATH.pumpdetail')),
            ],
        ),
    ]
