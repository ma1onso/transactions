from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tompany.companies.api.serializers import CompanyReadSerializer, CompanyWriteSerializer, \
    CompanyTransactionResumeSerializer
from tompany.companies.models import Company
from tompany.transactions.models import Transaction
from tompany.utils import ReadWriteSerializerMixin


class CompanyViewSet(
    ReadWriteSerializerMixin,
    GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
):
    queryset = Company.objects.all()
    read_serializer_class = CompanyReadSerializer
    write_serializer_class = CompanyWriteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(method='GET', responses={200: 'success'})
    @action(methods=['GET'], detail=True)
    def transaction_resume(self, request, *args, **kwargs):
        self.serializer_class = CompanyTransactionResumeSerializer

        company = self.get_object()
        company_resume = Transaction.objects.company_resume(company.pk)

        company_resume['company_name'] = company.name
        serializer = CompanyTransactionResumeSerializer(company_resume)

        return Response(serializer.data)
