from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.reverse import reverse

from mysite.models import Payment
from mysite.serializers import PaymentSerializer, UserSerializer
from mysite.permissions import IsOwnerOrReadOnly


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

    def perform_create(self, serializer):
        serializer.save(payer=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
