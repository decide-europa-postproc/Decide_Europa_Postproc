# Generated by Django 2.0 on 2018-12-20 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixnet', '0004_auto_20180605_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p', models.CharField(default=0, max_length=10)),
                ('g', models.CharField(default=0, max_length=10)),
                ('n', models.CharField(default=0, max_length=10)),
            ],
        ),
    ]
