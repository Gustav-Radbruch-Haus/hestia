from django.contrib import admin
from .models import Account, Transaction, Receipt, State, Tag

# Register your models here.
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Receipt)
admin.site.register(State)
admin.site.register(Tag)