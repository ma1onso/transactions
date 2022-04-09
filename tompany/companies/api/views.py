from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from tompany.companies.api.serializers import CompanyReadSerializer, CompanyWriteSerializer
from tompany.companies.models import Company
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

    def get_queryset(self):
        return Company.objects.all()
