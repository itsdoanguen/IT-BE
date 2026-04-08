from rest_framework.routers import DefaultRouter

from modules.profiles.views import HoSoCongTyViewSet, HoSoUngVienViewSet

router = DefaultRouter()
router.register(r"candidate", HoSoUngVienViewSet, basename="candidate-profiles")
router.register(r"company", HoSoCongTyViewSet, basename="company-profiles")

urlpatterns = router.urls
