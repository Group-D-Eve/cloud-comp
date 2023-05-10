# Generated by Django 3.0.6 on 2020-09-06 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Inventory Name')),
                ('quan_in_stock', models.IntegerField(verbose_name='Total In')),
                ('sales_quan', models.IntegerField(verbose_name='Total out')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Inventory',
                'verbose_name_plural': 'Inventorys',
            },
        ),
    ]