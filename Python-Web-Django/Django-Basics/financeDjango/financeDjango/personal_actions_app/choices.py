from django.db import models


class TransactionTypes(models.TextChoices):
    INCOME = 'Income', 'Income'
    EXPENSE = 'Expense', 'Expense'