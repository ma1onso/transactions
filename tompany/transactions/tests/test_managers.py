from model_bakery import baker

from django.test import TestCase

from tompany.transactions.models import Transaction


class TransactionManagerTestCase(TestCase):
    def setUp(self) -> None:
        self.transactions = baker.make("transactions.Transaction", status=Transaction.Status.REVERSED, _quantity=4)

    def test_resume_without_data(self):
        Transaction.objects.all().delete()

        self.assertDictEqual(Transaction.objects.resume(), {
            "company_with_more_sales": "",
            "company_with_less_sales": "",
            "total_transactions_charged": None,
            "total_transactions_not_charged": None,
            "company_with_more_transactions_not_charged": "",
        })

    def test_company_with_more_sales(self):
        self.assertNotEqual(Transaction.objects.company_with_more_sales(), "")
    
    def test_company_with_less_sales(self):
        self.assertNotEqual(Transaction.objects.company_with_less_sales(), "")
    
    def test_total_transactions_charged(self):
        self.assertNotEqual(Transaction.objects.total_transactions_charged(), 0)
    
    def test_total_transactions_not_charged(self):
        self.assertNotEqual(Transaction.objects.total_transactions_not_charged(), 0)
    
    def test_company_with_more_transactions_not_charged(self):
        self.assertNotEqual(Transaction.objects.company_with_more_transactions_not_charged(), "")

    def test_transactions_charged(self):
        transactions = baker.make(
            "transactions.Transaction", status=Transaction.Status.CLOSED, approval_status=Transaction.ApprovalStatus.CHARGED,
            _quantity=3
        )
        
        self.assertEqual(Transaction.objects.transactions_charged().count(), 3)
    
    def test_transactions_not_charged(self):
        self.assertEqual(Transaction.objects.transactions_not_charged().count(), 4)
     