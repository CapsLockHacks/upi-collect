# Generated by Django 2.2.6 on 2019-10-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upi', '0010_auto_20191019_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
