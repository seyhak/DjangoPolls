# Generated by Django 2.2.6 on 2019-10-07 17:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(default='My business', max_length=40)),
                ('address', models.TextField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Product', max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('notes', models.CharField(blank=True, max_length=300)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductsGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('notes', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(default='Review', max_length=30)),
                ('details', models.CharField(max_length=500)),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('reviewedProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestIT.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ManyToManyField(max_length=30, to='RestIT.ProductsGroup'),
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('address', models.TextField(blank=True, max_length=100)),
                ('ownerID', models.ManyToManyField(blank=True, to='RestIT.Business')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='business',
            name='owners',
            field=models.ManyToManyField(blank=True, to='RestIT.BusinessUser'),
        ),
    ]
