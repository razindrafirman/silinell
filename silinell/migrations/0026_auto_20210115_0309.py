# Generated by Django 3.1.3 on 2021-01-15 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silinell', '0025_auto_20210115_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='group',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]