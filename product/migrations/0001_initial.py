# Generated by Django 3.1.1 on 2020-09-19 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('subcategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=15)),
                ('itemShortDesc', models.CharField(max_length=60)),
                ('itemDetail', models.CharField(max_length=50)),
                ('MRP', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('sellMRP', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('imageUrl', models.ImageField(upload_to='product')),
                ('orderId', models.CharField(max_length=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategory.subcategory')),
            ],
        ),
    ]
