from django.contrib import admin
from .models import Account, Transaction, Receipt, State, Tag

# Register your models here.
admin.register(Account)
admin.register(Transaction)
admin.register(Receipt)
admin.register(State)
admin.register(Tag)