# Generated by Django 3.1.3 on 2020-12-31 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silinell', '0007_auto_20210101_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='status_webstie',
            field=models.CharField(choices=[('Down', 'Down'), ('Up', 'up')], max_length=40),
        ),
    ]
