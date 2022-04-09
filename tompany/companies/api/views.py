from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tompany.companies.api.serializers import CompanyReadSerializer, CompanyWriteSerializer, \
    CompanyTransactionResumeSerializer, EmptySerializer
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

    @swagger_auto_schema(method='GET', responses={200: CompanyTransactionResumeSerializer})
    @action(methods=['GET'], detail=True)
    def transaction_resume(self, request, *args, **kwargs):
        self.serializer_class = CompanyTransactionResumeSerializer

        company = self.get_object()
        company_resume = Transaction.objects.company_resume(company.pk)

        company_resume['company_name'] = company.name
        serializer = CompanyTransactionResumeSerializer(company_resume)

        return Response(serializer.data)

    @swagger_auto_schema(method='PATCH', request_body=EmptySerializer)
    @action(methods=['PATCH'], detail=True, url_path='transfer_transactions/(?P<target_company_id>\w+)')
    def transfer_transactions(self, request, *args, **kwargs):
        """ Transfer transactions from one company to another
        """
        company = self.get_object()
        target_company_id = kwargs.get('target_company_id')

        if not target_company_id:
            return Response({'error': 'target_company_id is required'}, status=400)

        target_company = Company.objects.get(pk=target_company_id)
        company.transactions.update(company=target_company)

        return Response(f'Transactions transferred successfully, from {company.name} to {target_company.name}')
