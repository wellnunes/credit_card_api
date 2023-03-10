from django.urls import path
from .views import CreditCardCreateView, CreditCardDetailView, CreditCardListView

app_name = 'credit_cards'

urlpatterns = [
    path('credit_card/', CreditCardListView.as_view(), name='credit-card-list'),
    path('credit_card/<int:pk>/', CreditCardDetailView.as_view(), name='credit-card-detail'),
    path('credit_card/create/', CreditCardCreateView.as_view(), name='credit-card-create'),

]
