from django.contrib import admin

from tompany.companies.models import Company
from tompany.transactions.admin import InlineTransaction


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active',)
    search_fields = ('name',)
    list_filter = ('is_active', 'is_orphan', )
    inlines = [InlineTransaction]
