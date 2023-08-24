# Generated by Django 2.2.22 on 2023-08-17 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20230817_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.Product'),
        ),
    ]
