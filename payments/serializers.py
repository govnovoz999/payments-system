from rest_framework import serializers

class BankWebhookSerializer(serializers.Serializer):
    operation_id = serializers.UUIDField()
    amount = serializers.IntegerField(min_value=0)
    payer_inn = serializers.CharField(max_length=12)
    document_number = serializers.CharField()
    document_date = serializers.DateTimeField()

class BalanceSerializer(serializers.Serializer):
    inn = serializers.CharField()
    balance = serializers.IntegerField()