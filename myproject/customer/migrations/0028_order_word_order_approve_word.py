# Generated by Django 4.1.5 on 2023-03-26 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0027_alter_order_approve_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='word',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order_approve',
            name='word',
            field=models.CharField(max_length=255, null=True),
        ),
    ]