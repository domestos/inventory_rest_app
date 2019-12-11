# Generated by Django 2.2.4 on 2019-12-10 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('sname', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='TypeDivece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Type of Divece',
                'verbose_name_plural': 'Type of Diveces',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(max_length=30)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Location')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Person')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.TypeDivece')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
    ]
