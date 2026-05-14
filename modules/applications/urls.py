from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modules.applications.views import UngTuyenViewSet

router = DefaultRouter()
router.register(r'', UngTuyenViewSet, basename='applications')

urlpatterns = [
    path('', include(router.urls)),
]
