# Generated by Django 4.0.5 on 2022-07-23 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='Total_money',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
