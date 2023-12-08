# Generated by Django 4.0.3 on 2022-06-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cUID', models.CharField(default='', max_length=50)),
                ('mdt', models.DateTimeField(auto_now=True)),
                ('cHistory', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Client_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cUid', models.CharField(default='', max_length=50)),
                ('mdt', models.DateTimeField(auto_now=True)),
                ('favorite', models.TextField(default='')),
            ],
        ),
    ]