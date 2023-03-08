# Generated by Django 3.2.18 on 2023-03-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_date', models.DateField(verbose_name='Expiration Date')),
                ('holder', models.CharField(max_length=50, verbose_name='Card Holder')),
                ('number', models.CharField(max_length=100, verbose_name='Card Number')),
                ('cvv', models.IntegerField(verbose_name='CVV')),
                ('brand', models.CharField(max_length=12, verbose_name='Card Brand')),
            ],
        ),
    ]