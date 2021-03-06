# Generated by Django 3.2.7 on 2021-09-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('polygon_id', models.IntegerField()),
                ('text', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon_id', models.IntegerField()),
                ('coordinates', models.CharField(max_length=200)),
                ('polygon_class', models.IntegerField()),
            ],
        ),
    ]
