from rest_framework import routers
from .views import PortfolioViewSet, ContactViewSet, TeamViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'team', TeamViewSet)
router.register(r'client', ClientViewSet)

urlpatterns = router.urls
