# Generated by Django 4.2 on 2025-05-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/imgres?q=placeholder%20food%20image&imgurl=https%3A%2F%2Fwww.food4fuel.com%2Fwp-content%2Fuploads%2Fwoocommerce-placeholder-600x600.png&imgrefurl=https%3A%2F%2Fwww.food4fuel.com%2Fproduct%2F21-day-plan-delivery%2F&docid=yjCHgS76Taov4M&tbnid=PQXxfAMSCvrEkM&w=600&h=600&hcb=2', max_length=500),
        ),
    ]
