from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Organization, Payment, BalanceLog
from .serializers import BankWebhookSerializer

from django.db import transaction

class BankWebhookView(APIView):
    def post(self, request):
        serializer = BankWebhookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        if Payment.objects.filter(operation_id=data["operation_id"]).exists():
            return Response(status=status.HTTP_200_OK)

        with transaction.atomic():
            org, _ = Organization.objects.get_or_create(inn=data["payer_inn"])
            org = Organization.objects.select_for_update().get(pk=org.pk)

            old = org.balance
            new = old + data["amount"]

            payment = Payment.objects.create(
                operation_id=data["operation_id"],
                organization=org,
                amount=data["amount"],
                document_number=data["document_number"],
                document_date=data["document_date"]
            )

            org.balance = new
            org.save()

            BalanceLog.objects.create(
                organization=org,
                payment=payment,
                old_balance=old,
                new_balance=new
            )

        return Response(status=status.HTTP_200_OK)

class BalanceView(APIView):
    def get(self, request, inn):
        try:
            org = Organization.objects.get(inn=inn)
            return Response({"inn": org.inn, "balance": org.balance})
        except Organization.DoesNotExist:
            return Response({"detail": "Not found"}, status=404)
