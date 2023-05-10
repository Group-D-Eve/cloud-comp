# Generated by Django 4.0.4 on 2022-04-18 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='partCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=150, verbose_name='part category')),
            ],
        ),
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='unitMeasure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unit', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('pocName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personOfContact', to='api.people')),
            ],
        ),
    ]