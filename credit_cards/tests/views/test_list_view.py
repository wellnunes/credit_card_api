from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from credit_cards.models import CreditCard
from credit_cards.serializers import CreditCardSerializer


class CreditCardListViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='usertest',
            password='passwordtest'
        )
        self.client.force_authenticate(user=self.user)
        self.credit_card1 = CreditCard(
            exp_date=datetime(2026, 12, 31).date(),
            holder="Example Holder 1",
            number="4539578763621486",
            cvv=123,
            brand="visa"
        )
        self.credit_card2 = CreditCard(
            exp_date=datetime(2026, 1, 31).date(),
            holder="Example Holder 2",
            number="5376517585680273",
            cvv=321,
            brand="master"
        )
        self.serializer1 = CreditCardSerializer(instance=self.credit_card1)
        self.serializer2 = CreditCardSerializer(instance=self.credit_card2)

    def test_get_all_credit_cards(self):
        """ This test check get all credit_cards """
        response = self.client.get(reverse('credit_card:credit-card-list'))
        credit_cards = CreditCard.objects.all()
        serializer = CreditCardSerializer(credit_cards, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
