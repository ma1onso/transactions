from django.contrib import admin

from tompany.transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'price', 'date_time',)
    list_filter = ('company__name',)
    raw_id_fields = ('company',)


class InlineTransaction(admin.TabularInline):
    model = Transaction
    extra = 0
