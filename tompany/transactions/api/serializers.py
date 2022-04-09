from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from tompany.transactions.models import Transaction


class TransactionReadSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionWriteSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['status', 'approval_status']


class TransactionResumeSerializer(Serializer):
    company_with_more_sales = serializers.CharField()
    company_with_less_sales = serializers.CharField()
    total_transactions_charged = serializers.FloatField()
    total_transactions_not_charged = serializers.FloatField()
    company_with_more_transactions_not_charged = serializers.CharField()
