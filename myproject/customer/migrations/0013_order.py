# Generated by Django 4.1.5 on 2023-03-13 12:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0012_addtocart_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('pageno', models.CharField(max_length=100)),
                ('mode', models.CharField(max_length=50)),
                ('order_date', models.DateField(default=datetime.date.today)),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('agency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.agencyprofile')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]