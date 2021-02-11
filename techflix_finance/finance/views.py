from rest_framework import viewsets
from .serializers import FinanceSerializer, PaymentSerializer
from .models import Finance, Payment

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all().order_by('id')
    serializer_class = FinanceSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('id')
    serializer_class = PaymentSerializer
