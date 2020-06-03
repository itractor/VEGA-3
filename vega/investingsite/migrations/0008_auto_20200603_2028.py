# Generated by Django 3.0.6 on 2020-06-03 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investingsite', '0007_auto_20200603_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stock_earnings',
            new_name='currency',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_preferred_equity',
            new_name='earnings',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_total_assets',
            new_name='preferred_equity',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_shares_outstanding',
            new_name='shares_outstanding',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='stock_total_liabilities',
            new_name='total_assets',
        ),
        migrations.AddField(
            model_name='stock',
            name='total_liabilities',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=100),
        ),
    ]
