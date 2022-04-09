import csv

from django.core.management import BaseCommand

from tompany.companies.models import Company


class Command(BaseCommand):
    help = 'This command read a CSV transactions file and only load the companies to the database'

    def add_arguments(self, parser):
        parser.add_argument('--csv_file_path', type=str, required=True, help="""
            Absolute path to the CSV file to be loaded.
            Expected format:
            company	price	date	status_transaction	status_approved
            didi food	50	2021-01-09 12:45:56.419962-06	closed	FALSE
            rappi prime	0	2021-02-09 15:19:39.25477-06	reversed	TRUE
        """)
        parser.add_argument('--debug_mode', action='store_true', help='Enable debug mode')

    def handle(self, *args, **options):
        with open(options['csv_file_path']) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')

            company_names = []
            for row in csv_reader:
                company_names.append(row['company'])

            company_names = list(set(company_names))

            if options['debug_mode']:
                self.stdout.write(company_names.__str__())  # It's use __str__ to prevent an AttributeError
            else:
                if '' in company_names:
                    self.stdout.write('There is an empty company')
                    self.create_orphan_company()
                    company_names.remove('')

                self.create_company(company_names)

        self.stdout.write(self.style.SUCCESS('Command load_companies successfully executed'))

    def create_orphan_company(self):
        Company.objects.create_orphan()

    def create_company(self, company_names: list):
        for company_name in company_names:
            company, created = Company.objects.get_or_create(name=company_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Company {company_name} created in database'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Company {company_name} already exists in database'))
