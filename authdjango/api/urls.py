from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, test

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', test),
]