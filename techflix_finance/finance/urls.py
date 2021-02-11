from django.urls import include, path
from rest_framework import routers
from .views import FinanceViewSet, PaymentViewSet


router = routers.DefaultRouter()
router.register(r'finances', FinanceViewSet, basename="finances")
router.register(r'payment', PaymentViewSet, basename="payment")


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'
    )),
]