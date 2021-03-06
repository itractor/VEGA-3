# Generated by Django 3.0.6 on 2020-05-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investingsite', '0004_auto_20200527_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_earnings',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
    ]
