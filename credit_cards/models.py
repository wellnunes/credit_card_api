from django.db import models


class CreditCard(models.Model):
    exp_date = models.DateField("Expiration Date")
    holder = models.CharField("Card Holder", max_length=50)
    number = models.CharField("Card Number", max_length=100)
    cvv = models.IntegerField("CVV")
    brand = models.CharField("Card Brand", max_length=12)
