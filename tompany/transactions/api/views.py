from distutils.util import strtobool

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tompany.transactions.api.serializers import TransactionResumeSerializer, TransactionReadSerializer, TransactionWriteSerializer
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
    read_serializer_class = TransactionReadSerializer
    write_serializer_class = TransactionWriteSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["status", "approval_status"]

    @swagger_auto_schema(method='GET', responses={200: TransactionResumeSerializer}, manual_parameters=[
        openapi.Parameter("exclude_inactive_companies", openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN)
    ])
    @action(methods=['GET'], detail=False)
    def resume(self, request, *args, **kwargs):
        self.serializer_class = TransactionResumeSerializer
        exclude_inactive_companies = request.query_params.get('exclude_inactive_companies')

        if exclude_inactive_companies != None and strtobool(exclude_inactive_companies):
            resume_data = Transaction.objects_active.resume()
        else:
            resume_data = Transaction.objects.resume()

        serializer = TransactionResumeSerializer(resume_data)

        return Response(serializer.data)
