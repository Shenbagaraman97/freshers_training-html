# Generated by Django 2.2.12 on 2022-02-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'persons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
