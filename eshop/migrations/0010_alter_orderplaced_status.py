# Generated by Django 5.0.7 on 2024-07-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0009_payment_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Accepted'), ('Shipped', 'shipped'), ('On the way', 'On the way'), ('Out for delivery', 'out for delivery'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
    ]
