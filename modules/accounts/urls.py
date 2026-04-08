from rest_framework.routers import DefaultRouter

from modules.accounts.views import NguoiDungViewSet

router = DefaultRouter()
router.register(r"users", NguoiDungViewSet, basename="users")

urlpatterns = router.urls
