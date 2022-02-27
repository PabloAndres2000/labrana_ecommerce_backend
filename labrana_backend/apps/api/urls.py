from rest_framework import routers

from labrana_backend.apps.listelement.api.views.element import ElementViewSet
from labrana_backend.apps.listelement.api.views.category import CategoryViewSet
from labrana_backend.apps.listelement.api.views.type import TypeViewSet


router = routers.SimpleRouter()

router.register(r"listelements/element", ElementViewSet, basename="element")
router.register(r"listelements/category", CategoryViewSet, basename="category")
router.register(r"listelements/type", TypeViewSet, basename="type")

urlpatterns = router.urls
