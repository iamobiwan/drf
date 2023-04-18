from django.shortcuts import render
from rest_framework import mixins, viewsets, permissions
from .models import Product
from .serializer import ProductSerializer
from django.core.mail import EmailMessage
from django.conf import settings

viewsets.ModelViewSet

# Create your views here.
class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


def test(request):
    email = EmailMessage(
        'Test Header',
        'Test Message',
        settings.EMAIL_HOST_USER,
        ['devbox@list.ru']
    )
    email.fail_silently = False
    email.send()