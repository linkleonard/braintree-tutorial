from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from mysite import views

router = DefaultRouter()
router.register(r'payments', views.PaymentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'payments/client_token/', views.client_token, name='payment-nonce'),
    url(r'^', include(router.urls)),
]
