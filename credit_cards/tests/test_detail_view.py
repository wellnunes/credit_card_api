from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from credit_cards.models import CreditCard
from credit_cards.serializers import CreditCardSerializer


class CreditCardDetailViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='usertest',
            password='passwordtest'
        )
        self.client.force_authenticate(user=self.user)
        self.credit_card = CreditCard.objects.create(
            exp_date=datetime(2026, 12, 31).date(),
            holder="Example Holder",
            number="4539578763621486",
            cvv=123,
            brand="visa"
        )
        self.serializer = CreditCardSerializer(instance=self.credit_card)

    def test_valid_credit_card_detail(self):
        """ This test check valid credit card detail  """
        response = self.client.get(reverse('credit_card:credit-card-detail', kwargs={'pk': self.credit_card.pk}))
        credit_card = CreditCard.objects.get(pk=self.credit_card.pk)
        serializer = CreditCardSerializer(credit_card)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_credit_card_detail(self):
        """ This test check invalid credit card creation  """
        response = self.client.get(reverse('credit_card:credit-card-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
