# Generated by Django 4.1.4 on 2023-01-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0002_curd_delete_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curd',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
