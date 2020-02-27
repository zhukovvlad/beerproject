# Generated by Django 3.0.3 on 2020-02-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True, null=True)),
                ('og', models.FloatField(blank=True, null=True)),
                ('abv', models.FloatField(blank=True, null=True)),
                ('ibu', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
