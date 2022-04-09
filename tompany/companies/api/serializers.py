from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from tompany.companies.models import Company


class CompanyReadSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyWriteSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'is_active']


class CompanyTransactionResumeSerializer(Serializer):
    company_name = serializers.CharField()
    total_transactions_charged = serializers.FloatField()
    total_transactions_not_charged = serializers.FloatField()
    date_with_more_transactions = serializers.DateField()


class EmptySerializer(Serializer):
    pass
