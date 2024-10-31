# Generated by Django 4.2.16 on 2024-10-31 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Refno', models.IntegerField(primary_key='Refno', serialize=False)),
                ('percentage', models.FloatField()),
                ('DoB', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
