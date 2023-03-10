# Generated by Django 3.2.18 on 2023-03-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='brand',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Card Brand'),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.IntegerField(blank=True, null=True, verbose_name='CVV'),
        ),
    ]
