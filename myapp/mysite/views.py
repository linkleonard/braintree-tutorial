from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from django.conf import settings

from mysite.models import Payment
from mysite.serializers import PaymentSerializer, UserSerializer
from mysite.permissions import IsOwnerOrReadOnly

import braintree


braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    settings.BRAINTREE['merchant_id'],
    settings.BRAINTREE['public_key'],
    settings.BRAINTREE['private_key'],
    )


class PaymentFailed(APIException):
    status_code = 403
    default_detail = "Payment failed. Please try again later."


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
        )

    def perform_create(self, serializer):
        # Ignore if user submits invalid data.
        if serializer.is_valid():
            result = braintree.Transaction.sale({
                'amount': serializer.validated_data['amount'],
                'payment_method_nonce': serializer.validated_data['payment_method_nonce'],  # noqa
            })

            if result.is_success:
                serializer.save(payer=self.request.user)
            else:
                # The payment failed.
                # TODO: Handle it via Rollbar, logging, etc...
                raise PaymentFailed()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def client_token(request):
    return Response({'token': braintree.ClientToken.generate()})
