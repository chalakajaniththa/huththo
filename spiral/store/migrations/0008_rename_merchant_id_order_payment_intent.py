# Generated by Django 4.1.2 on 2022-10-27 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_orderitem_delete_orderitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='payment_intent',
        ),
    ]