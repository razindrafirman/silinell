# Generated by Django 3.1.3 on 2021-01-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silinell', '0023_auto_20210114_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='group',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='component',
            name='status',
            field=models.CharField(choices=[('Operational', 'Operational'), ('Perfomance Issue', 'Perfomance Issue'), ('Partial Outage', 'Partial Outage'), ('Major Outage', 'Major Outage')], max_length=40),
        ),
    ]