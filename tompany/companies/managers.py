from django.db.models import Manager


class CompanyManager(Manager):
    def create_orphan(self):
        """ Create a new company without name
        """
        return self.get_or_create(
            name='Orphan_company',
            defaults={
                'is_orphan': True,
            }
        )
