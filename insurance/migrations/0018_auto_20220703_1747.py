# Generated by Django 3.0.5 on 2022-07-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0017_auto_20220702_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spsc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codunspsc', models.CharField(max_length=30)),
                ('nomunspsc', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='polizatemp',
            name='nomunspsc',
            field=models.CharField(max_length=300),
        ),
    ]
