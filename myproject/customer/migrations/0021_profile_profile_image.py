# Generated by Django 4.1.5 on 2023-03-18 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_remove_profile1_user_delete_key_delete_profile1'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
