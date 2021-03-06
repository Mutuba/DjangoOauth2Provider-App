# Generated by Django 2.2.9 on 2020-04-09 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductinOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='orders.ProductinOrder', to='products.Product'),
        ),
    ]
