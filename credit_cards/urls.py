from rest_framework import routers
from django.urls import path, include

from credit_cards.views import CreditCardViewSet

router = routers.DefaultRouter()
router.register('credit_card', CreditCardViewSet)

app_name = 'credit_cards'

urlpatterns = [
    path('', include(router.urls)),
]
