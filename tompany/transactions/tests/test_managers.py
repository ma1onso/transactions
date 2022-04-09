from django.test import TestCase

from tompany.transactions.models import Transaction


class TransactionManagerTestCase(TestCase):
    def test_resume_without_data(self):
        self.assertDictEqual(Transaction.objects.resume(), {
            "company_with_more_sales": 0,
            "company_with_less_sales": 0,
            "total_transactions_charged": None,
            "total_transactions_not_charged": None,
            "company_with_more_transactions_not_charged": 0,
        })
