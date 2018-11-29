# Generated by Django 2.1.3 on 2018-11-29 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(default='', max_length=30)),
                ('name', models.CharField(default='', max_length=30)),
                ('script_id', models.IntegerField(default=0)),
                ('script', models.TextField(default='')),
            ],
        ),
    ]
