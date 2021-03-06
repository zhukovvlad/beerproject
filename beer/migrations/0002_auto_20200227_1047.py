# Generated by Django 3.0.3 on 2020-02-27 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name="Brewery's name")),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('alpha_min', models.FloatField(blank=True, null=True)),
                ('alpha_max', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(blank=True, max_length=40, null=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='beer',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='beer',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='beer',
            name='description',
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brewered', to='beer.Brewery'),
        ),
        migrations.AddField(
            model_name='beer',
            name='hops',
            field=models.ManyToManyField(blank=True, related_name='used_hops', to='beer.Hop'),
        ),
        migrations.AddField(
            model_name='beer',
            name='style',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='beer.Style'),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(choices=[(1, '👍'), (-1, '👎')])),
                ('voted_on', models.DateTimeField(auto_now=True)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Beer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'beer')},
            },
        ),
    ]
