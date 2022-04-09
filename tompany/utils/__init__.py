from django.core.management import BaseCommand


class TransactionCSVCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--csv_file_path', type=str, required=True, help="""
            Absolute path to the CSV file to be loaded.
            Expected format:
            company	price	date	status_transaction	status_approved
            didi food	50	2021-01-09 12:45:56.419962-06	closed	FALSE
            rappi prime	0	2021-02-09 15:19:39.25477-06	reversed	TRUE
        """)
        parser.add_argument('--debug_mode', action='store_true', help='Enable debug mode')
