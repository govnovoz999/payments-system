from django.urls import path
from .views import BankWebhookView, BalanceView

urlpatterns = [
    path('webhook/bank/', BankWebhookView.as_view()),
    path('organizations/<str:inn>/balance/', BalanceView.as_view()),
]
