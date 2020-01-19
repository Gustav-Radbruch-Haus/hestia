from django.db import models
from .account import Account
from .tag import Tag
from .state import State
from .receipt import Receipt


class TransactionManager(models.Manager):
    def get_transactions_for(self, account):
        return super().get_queryset().filter(account=account)

    def get_balance_for(self, account):
        transactions = self.get_transactions_for(account)
        balance = Decimal(0)
        for transaction in transactions:
            balance = balance + transaction.amount
        return balance

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        verbose_name="creation_date", auto_now_add=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    subject = models.CharField(
        verbose_name="transaction_subject", max_length=128)
    date = models.DateTimeField(verbose_name="transaction_date")
    sender = models.CharField(max_length=64)
    receiver = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    receipt = models.ForeignKey(Receipt,verbose_name="transaction_receipt", on_delete=models.PROTECT)

    objects = TransactionManager()

    def __str__(self):
        return self.account + " " + self.date + " from " + self.sender + " to " + self.receiver + " :" + self.amount

