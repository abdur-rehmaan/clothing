# Generated by Django 2.2.22 on 2023-08-16 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_auto_20230816_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='orderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.product')),
            ],
        ),
        migrations.CreateModel(
            name='shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=300)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=8)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='categories',
        ),
        migrations.RemoveField(
            model_name='newarrival',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_contact',
            new_name='customer_email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='customer',
            name='cst',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='cart',
        ),
        migrations.DeleteModel(
            name='newarrival',
        ),
        migrations.AddField(
            model_name='shipping',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.customer'),
        ),
    ]
