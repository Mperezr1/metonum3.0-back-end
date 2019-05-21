from rest_framework import routers

from .viewsets import EcuacionesNoLinealesViewSet


router = routers.SimpleRouter()
router.register('ecuacionesNoLineales', EcuacionesNoLinealesViewSet)

urlpatterns = router.urls
