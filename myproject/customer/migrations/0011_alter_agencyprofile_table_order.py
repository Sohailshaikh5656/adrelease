# Generated by Django 4.1.5 on 2023-03-11 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_profile_user_agencyprofile'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='agencyprofile',
            table='Agencyprofile',
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('description', models.TextField()),
                ('agency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.agencyprofile')),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.profile')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
