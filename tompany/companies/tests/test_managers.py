from django.conf import settings
from django.test import TestCase

from tompany.companies.models import Company


class CompanyTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_orphan_company(self):
        Company.objects.create_orphan()

        self.assertEqual(Company.objects.filter(name=settings.ORPHAN_COMPANY_NAME).count(), 1)
