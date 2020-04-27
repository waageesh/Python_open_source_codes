# Generated by Django 3.0.4 on 2020-04-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Covid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observationdate', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('lastupdate', models.CharField(max_length=30)),
                ('confirmed', models.CharField(max_length=30)),
                ('deaths', models.CharField(max_length=30)),
                ('recovered', models.CharField(max_length=30)),
            ],
        ),
    ]
