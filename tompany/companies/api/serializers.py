from rest_framework.serializers import ModelSerializer

from tompany.companies.models import Company


class CompanyReadSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyWriteSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'is_active']
