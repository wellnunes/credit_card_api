from datetime import datetime
from django.test import TestCase
from credit_cards.models import CreditCard
from credit_cards.serializers import CreditCardSerializer


class CreditCardSerializerTestCase(TestCase):

    def setUp(self):
        self.credit_card = CreditCard(
            exp_date=datetime(2026, 12, 31).date(),
            holder="Example Holder",
            number="4539578763621486",
            cvv=123,
            brand="visa"
        )
        self.serializer = CreditCardSerializer(instance=self.credit_card)

    def test_serialized_fields(self):
        """ This test check credit card serialized fields """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "exp_date", "holder", "number", "cvv", "brand"})
