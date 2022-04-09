from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tompany.companies.api.serializers import CompanyReadSerializer, CompanyWriteSerializer
from tompany.transactions.api.serializers import TransactionResumeSerializer
from tompany.transactions.models import Transaction
from tompany.utils import ReadWriteSerializerMixin


class TransactionViewSet(
    ReadWriteSerializerMixin,
    GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
):
    queryset = Transaction.objects.all()
    read_serializer_class = CompanyReadSerializer
    write_serializer_class = CompanyWriteSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(method='GET', responses={200: TransactionResumeSerializer})
    @action(methods=['GET'], detail=False)
    def resume(self, request, *args, **kwargs):
        self.serializer_class = TransactionResumeSerializer
        serializer = TransactionResumeSerializer(Transaction.objects.resume())

        return Response(serializer.data)
