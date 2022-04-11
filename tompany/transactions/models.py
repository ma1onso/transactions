from django.db import models
from model_utils.models import TimeStampedModel

from tompany.transactions.managers import TransactionManager, ActiveTransactionManager


class Transaction(TimeStampedModel):
    class Status(models.TextChoices):
        CLOSED = 'closed', 'Closed'
        REVERSED = 'reversed', 'Reversed'
        PENDING = 'pending', 'Pending'
        FUNDING = 'funding', 'Funding'
        FUNDING_USER = 'funding_user', 'Funding User'

    class ApprovalStatus(models.TextChoices):
        CHARGED = 'charged', 'Charged'
        NOT_CHARGED = 'not_charged', 'Not Charged'

    price = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    date_time = models.DateTimeField(
        help_text='Date and time of transaction',
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    approval_status = models.CharField(
        max_length=20,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.NOT_CHARGED,
    )
    # External keys
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='transactions',
    )

    objects = TransactionManager()
    objects_active = ActiveTransactionManager()

    def is_paid(self):
        if self.status == self.Status.CLOSED and self.approval_status == self.ApprovalStatus.CHARGED:
            return True
        return False
