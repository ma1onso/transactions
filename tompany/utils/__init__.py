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


class ReadWriteSerializerMixin(object):
    """
    Overrides get_serializer_class to choose the read serializer
    for GET requests and the write serializer for POST requests.

    Set read_serializer_class and write_serializer_class attributes on a
    viewset.
    """

    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.get_write_serializer_class()
        return self.get_read_serializer_class()

    def get_read_serializer_class(self):
        assert self.read_serializer_class is not None, (
            "'%s' should either include a `read_serializer_class` attribute,"
            "or override the `get_read_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.read_serializer_class

    def get_write_serializer_class(self):
        assert self.write_serializer_class is not None, (
            "'%s' should either include a `write_serializer_class` attribute,"
            "or override the `get_write_serializer_class()` method."
            % self.__class__.__name__
        )
        return self.write_serializer_class
