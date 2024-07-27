# Generated by Django 4.1.5 on 2023-03-11 10:30

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_alter_newadtype_agency'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0011_alter_agencyprofile_table_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addtocart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('ad', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='agency.newadtype')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'add_to_cart',
            },
        ),
        migrations.DeleteModel(
            name='order',
        ),
    ]