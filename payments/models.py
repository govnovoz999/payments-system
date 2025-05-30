from django.db import models

class Organization(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    balance = models.BigIntegerField(default=0)

class Payment(models.Model):
    operation_id = models.UUIDField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    document_number = models.CharField(max_length=64)
    document_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class BalanceLog(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    old_balance = models.BigIntegerField()
    new_balance = models.BigIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
