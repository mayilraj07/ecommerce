# Generated by Django 5.0.7 on 2024-07-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0016_alter_customer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=200),
        ),
    ]
