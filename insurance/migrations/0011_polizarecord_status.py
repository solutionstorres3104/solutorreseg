# Generated by Django 3.0.5 on 2022-06-29 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0010_auto_20220629_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='polizarecord',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]
