from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Sum
from django.db.models.functions import Coalesce


class TransactionManager(BaseUserManager):
    def resume(self):
        return {
            "company_with_more_sales": self.company_with_more_sales(),
            "company_with_less_sales": self.company_with_less_sales(),
            "total_transactions_charged": self.total_transactions_charged(),
            "total_transactions_not_charged": self.total_transactions_not_charged(),
            "company_with_more_transactions_not_charged": self.company_with_more_transactions_not_charged(),
        }

    def company_with_more_sales(self):
        return self.company_sales().order_by('-price__sum').first()['company__name']

    def company_with_less_sales(self):
        return self.company_sales().order_by('price__sum').first()['company__name']

    def total_transactions_charged(self):
        return self.transactions_charged().aggregate(Sum('price'))['price__sum']

    def total_transactions_not_charged(self):
        return self.transactions_not_charged().aggregate(Sum('price'))['price__sum']

    def company_with_more_transactions_not_charged(self):
        return self.transactions_not_charged().values('company__name').annotate(
            Sum('price')
        ).order_by('-price__sum').first()['company__name']

    def transactions_charged(self):
        from tompany.transactions.models import Transaction

        return self.filter(
            status=Transaction.Status.CLOSED, approval_status=Transaction.ApprovalStatus.CHARGED
        )

    def transactions_not_charged(self):
        from tompany.transactions.models import Transaction

        return self.exclude(
            status=Transaction.Status.CLOSED, approval_status=Transaction.ApprovalStatus.CHARGED
        )

    def company_sales(self):
        return self.values('company__name').annotate(Sum('price'))
