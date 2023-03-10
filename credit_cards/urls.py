from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CreditCardCreateView, CreditCardDetailView, CreditCardListView

app_name = 'credit_cards'

schema_view = get_schema_view(
   openapi.Info(
      title="Credit Card API",
      default_version='v1',
      description="Simple API for registering and listing credit cards, with some number and brand validations",
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)

urlpatterns = [
    path('credit_card/', CreditCardListView.as_view(), name='credit-card-list'),
    path('credit_card/<int:pk>/', CreditCardDetailView.as_view(), name='credit-card-detail'),
    path('credit_card/create/', CreditCardCreateView.as_view(), name='credit-card-create'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
