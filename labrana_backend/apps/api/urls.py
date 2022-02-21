from rest_framework import routers

from labrana_backend.apps.listelement.api.views.element import ElementViewSet


router = routers.SimpleRouter()

router.register(r"listelements/element", ElementViewSet, basename="element")

urlpatterns = router.urls
