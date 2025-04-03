# loans/admin.py
from django.contrib import admin
from .models import Loan, PromissoryNote, LoanRegistration, Installment

admin.site.register(Loan)
admin.site.register(PromissoryNote)
admin.site.register(LoanRegistration)
admin.site.register(Installment)