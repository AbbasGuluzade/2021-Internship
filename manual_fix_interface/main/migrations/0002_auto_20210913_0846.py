# Generated by Django 3.2.7 on 2021-09-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='polygon_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='match',
            name='text',
            field=models.CharField(max_length=30),
        ),
    ]
