# Generated by Django 4.2.5 on 2024-03-24 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_comment_uploadtime_alter_menu_upload_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='upload_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='uploadTime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 24, 7, 1, 27, 425887, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='listingDate',
            field=models.DateField(default=datetime.datetime(2024, 3, 24, 7, 1, 27, 424911, tzinfo=datetime.timezone.utc)),
        ),
    ]