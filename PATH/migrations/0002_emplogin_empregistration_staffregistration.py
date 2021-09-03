# Generated by Django 3.1.7 on 2021-08-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PATH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empusername', models.CharField(max_length=100)),
                ('Emppassword', models.CharField(max_length=20)),
                ('status', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EmpRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empid', models.CharField(default='', max_length=10)),
                ('Empname', models.CharField(default='', max_length=100)),
                ('Empmail', models.EmailField(default='', max_length=50)),
                ('Empphone', models.IntegerField()),
                ('Pump', models.CharField(max_length=100)),
                ('Emppass', models.CharField(max_length=20)),
                ('status', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='staffRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(max_length=100)),
                ('staffpass', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]