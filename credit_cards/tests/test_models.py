from datetime import datetime
from django.test import TestCase
from credit_cards.models import CreditCard


class CreditCardModelTestCase(TestCase):

    def setUp(self):
        self.credit_card = CreditCard(
            exp_date=datetime(2026, 12, 31).date(),
            holder="Example Holder",
            number="4539578763621486",
            brand="visa"
        )

    def test_credit_card_attributes(self):
        """ This test check the creation of a credit card without a not required field (cvv) """
        self.assertEqual(self.credit_card.exp_date, datetime(2026, 12, 31).date())
        self.assertEqual(self.credit_card.holder, "Example Holder")
        self.assertEqual(self.credit_card.number, "4539578763621486")
        self.assertEqual(self.credit_card.brand, "visa")
        self.assertEqual(self.credit_card.cvv, None)
