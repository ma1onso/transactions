import csv

from dateutil import parser
from django.conf import settings

from tompany.utils import TransactionCSVCommand
from tompany.companies.models import Company
from tompany.transactions.models import Transaction


class Command(TransactionCSVCommand):
    help = 'This command read a CSV transactions file and save the transactions to database, ' \
           'also related with the company'

    def handle(self, *args, **options):
        with open(options['csv_file_path']) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            if options['debug_mode']:
                for row in csv_reader:
                    self.stdout.write(row.values().__str__())  # It's use __str__ to prevent an AttributeError
            else:
                for row in csv_reader:
                    self.create_transaction_for_company(row)

        self.stdout.write(self.style.SUCCESS(
            f'Command load_transactions successfully executed. Debug mode: {options["debug_mode"]}'
        ))

    def create_transaction_for_company(self, row):
        company_name = row['company'].lower()
        if company_name == '':
            company_name = settings.ORPHAN_COMPANY_NAME
        company = Company.objects.get(name=company_name)

        try:
            approval_status = Transaction.ApprovalStatus.CHARGED if 'true' == row['status_approved'].lower() \
                else Transaction.ApprovalStatus.NOT_CHARGED

            transaction, created = Transaction.objects.get_or_create(
                company=company,
                price=row['price'],
                date_time=parser.parse(row['date']),
                status=row['status_transaction'],
                approval_status=approval_status,
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Transaction created: {transaction}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Transaction already exists: {transaction}'))

        except Exception as exception:
            self.stdout.write(self.style.ERROR(f'Error creating transaction for company {company_name}'))
            self.stdout.write(self.style.ERROR(
                f"Transaction information: {row['price']} {row['date']} {row['status_transaction']} {row['status_approved']}"
            ))
            self.stdout.write(self.style.ERROR(f'Exception error: {exception}'))
