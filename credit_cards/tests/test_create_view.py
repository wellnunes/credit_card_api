from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from credit_cards.models import CreditCard


class CreditCardCreateViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='usertest',
            password='passwordtest'
        )
        self.client.force_authenticate(user=self.user)
        self.valid_payload = {
            'exp_date': '02/2026',
            'holder': 'Example Holder 1',
            'number': '4539578763621486',
            'cvv': '123',
        }
        self.invalid_payload = {
            'exp_date': '02/2026',
            'holder': 'Example Holder 2',
            'number': '1111111111111111',
            'cvv': 123,
        }

    def test_valid_credit_card_creation(self):
        """ This test check valid credit card creation  """
        response = self.client.post(
            reverse('credit_card:credit-card-create'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CreditCard.objects.count(), 1)
        self.assertEqual(CreditCard.objects.get().holder, 'Example Holder 1')

    def test_invalid_credit_card_creation(self):
        """ This test check invalid credit card creation """
        response = self.client.post(
            reverse('credit_card:credit-card-create'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
