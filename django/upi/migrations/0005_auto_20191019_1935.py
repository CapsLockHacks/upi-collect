# Generated by Django 2.2.6 on 2019-10-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upi', '0004_auto_20191019_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=18, unique=True),
        ),
    ]
