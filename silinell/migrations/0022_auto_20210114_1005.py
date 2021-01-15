# Generated by Django 3.1.3 on 2021-01-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silinell', '0021_auto_20210114_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component_group',
            name='status',
        ),
        migrations.AddField(
            model_name='component_group',
            name='visibility',
            field=models.CharField(choices=[('Always expanded', 'Always expanded'), ('Always collapse', 'Always collapse'), ('Collapse but expand if there are issues', 'Collapse but expand if there are issues')], default='Always expanded', max_length=40),
        ),
    ]
