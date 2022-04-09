from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tompany.companies.api.views import CompanyViewSet
from tompany.transactions.api.views import TransactionViewSet
from tompany.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("companies", CompanyViewSet)
router.register("transactions", TransactionViewSet)


app_name = "api"
urlpatterns = router.urls
