# Generated by Django 5.2.4 on 2025-07-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backtester', '0003_alter_trade_gain_percentage_alter_trade_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinpairslist',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
