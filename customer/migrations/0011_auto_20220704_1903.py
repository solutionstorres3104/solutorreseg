# Generated by Django 3.0.5 on 2022-07-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20220704_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='codunspsc',
        ),
        migrations.AddField(
            model_name='customer',
            name='spsc',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
