import csv

from tompany.utils import TransactionCSVCommand
from tompany.companies.models import Company


class Command(TransactionCSVCommand):
    help = 'This command read a CSV transactions file and only save the companies to the database'

    def handle(self, *args, **options):
        with open(options['csv_file_path']) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            company_names = []
            for row in csv_reader:
                company_names.append(row['company'].lower())

            # Remove duplicates (automatically)
            company_names = list(set(company_names))

            if options['debug_mode']:
                self.stdout.write(company_names.__str__())  # It's use __str__ to prevent an AttributeError
            else:
                if '' in company_names:
                    self.stdout.write('There is an empty company')
                    self.create_orphan_company()
                    company_names.remove('')

                self.create_companies(company_names)

        self.stdout.write(self.style.SUCCESS(
            f'Command load_companies successfully executed. Debug mode: {options["debug_mode"]}'
        ))

    def create_orphan_company(self):
        Company.objects.create_orphan()

    def create_companies(self, company_names: list):
        for company_name in company_names:
            company, created = Company.objects.get_or_create(name=company_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Company {company_name} created in database'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Company {company_name} already exists in database'))
