# Generated by Django 2.0.2 on 2018-03-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20180301_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='monthly_payments',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
        ),
        migrations.AlterField(
            model_name='input',
            name='bond_term',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
        ),
        migrations.AlterField(
            model_name='input',
            name='deposit_paid',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
        ),
        migrations.AlterField(
            model_name='input',
            name='fixed_interest_rate',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
        ),
        migrations.AlterField(
            model_name='input',
            name='name_to_save',
            field=models.CharField(default='Results', max_length=500),
        ),
        migrations.AlterField(
            model_name='input',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=19),
        ),
    ]
