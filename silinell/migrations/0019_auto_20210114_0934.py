# Generated by Django 3.1.3 on 2021-01-14 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silinell', '0018_delete_historical_del_incident'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='group',
            field=models.CharField(max_length=40),
        ),
    ]
