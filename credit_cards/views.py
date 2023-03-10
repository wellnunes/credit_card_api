from rest_framework import generics, permissions
from credit_cards.models import CreditCard
from credit_cards.serializers import CreditCardSerializer


class CreditCardListView(generics.ListAPIView):
    """ List View w/ auth required permissions to list all credit cards """
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditCardCreateView(generics.CreateAPIView):
    """ Create View w/ auth required permissions to create credit cards if they are valid """
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditCardDetailView(generics.RetrieveAPIView):
    """ Detail View w/ auth required permissions to detail selected credit card by id """
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]
