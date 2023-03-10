from rest_framework import generics, permissions
from credit_cards.models import CreditCard
from credit_cards.serializers import CreditCardSerializer


class CreditCardListView(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditCardCreateView(generics.CreateAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreditCardDetailView(generics.RetrieveAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = [permissions.IsAuthenticated]
