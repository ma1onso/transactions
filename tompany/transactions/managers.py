from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Sum, Count


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
        try:
            return self.company_sales().order_by('-price__sum').first()['company__name']
        except TypeError:
            return ""

    def company_with_less_sales(self):
        try:
            self.company_sales().order_by('price__sum').first()['company__name']
        except TypeError:
            return ""

    def total_transactions_charged(self):
        try:
            return self.transactions_charged().aggregate(Sum('price'))['price__sum']
        except TypeError:
            return 0

    def total_transactions_not_charged(self):
        try:
            return self.transactions_not_charged().aggregate(Sum('price'))['price__sum']
        except TypeError:
            return 0

    def company_with_more_transactions_not_charged(self):
        try:
            return self.transactions_not_charged().values('company__name').annotate(
                Sum('price')
            ).order_by('-price__sum').first()['company__name']
        except TypeError:
            return ""

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

    def company_resume(self, company_id):
        return {
            "total_transactions_charged": self.transactions_charged_by_company(
                company_id
            ).aggregate(Sum('price'))['price__sum'],
            "total_transactions_not_charged": self.transactions_not_charged_by_company(
                company_id
            ).aggregate(Sum('price'))['price__sum'],
            "date_with_more_transactions": self.date_with_more_transactions(company_id),
        }

    def transactions_charged_by_company(self, company_id):
        return self.transactions_charged().filter(company_id=company_id)

    def transactions_not_charged_by_company(self, company_id):
        return self.transactions_not_charged().filter(company_id=company_id)

    def date_with_more_transactions(self, company_id):
        return self.filter(company_id=company_id).values(
            'date_time__date'
        ).annotate(Count('id')).order_by('-id__count').first()['date_time__date']
