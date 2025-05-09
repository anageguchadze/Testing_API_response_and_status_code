from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrivateItemViewSet

router = DefaultRouter()
router.register(r'private-items', PrivateItemViewSet, basename='privateitem')

urlpatterns = [
    path('api/', include(router.urls)),
]
