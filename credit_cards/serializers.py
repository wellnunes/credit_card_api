from rest_framework import serializers

from credit_cards.models import CreditCard


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['exp_date', 'holder', 'number', 'cvv', 'brand']
