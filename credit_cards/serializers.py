import calendar
from datetime import datetime
from rest_framework import serializers
from django.core.validators import RegexValidator
from creditcard import CreditCard as CreditCardCheck
from credit_cards.models import CreditCard


class CreditCardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    exp_date = serializers.DateField(input_formats=['%m/%Y'])
    holder = serializers.CharField(min_length=2)
    number = serializers.CharField()
    cvv = serializers.CharField(required=False, min_length=3, max_length=4, validators=[RegexValidator(r'^\d{1,10}$')])
    brand = serializers.CharField(read_only=True)

    def create(self, validated_data):
        """ when creating, we will check the validity of the date and the credit card, in addition to assigning the
         corresponding mark and encrypting the cc number when saving in the db """
        credit_card = CreditCardCheck(validated_data.get('number'))
        if credit_card.is_valid():
            validated_data['brand'] = credit_card.get_brand()
            exp_date = validated_data['exp_date']
            if exp_date > datetime.today().date():
                validated_data['exp_date'] = exp_date.replace(day=calendar.monthrange(exp_date.year, exp_date.month)[1])
                return CreditCard.objects.create(**validated_data)
            raise serializers.ValidationError("A data não pode ser menor do que a data de hoje")
        raise serializers.ValidationError("Número do cartão inválido")
