# myapi/urls.pyfrom django.urls import include, path
from rest_framework import routers
from .views import DepartmentViewSet, labViewSet, ComputerViewSet, EquipmentViewSet, SoftwareViewSet, PerchaseViewSet

from django.urls import path, include


router = routers.DefaultRouter()

# list api view set here
router.register(r'departments', DepartmentViewSet)
router.register(r'labs', labViewSet)
router.register(r'computers', ComputerViewSet)
router.register(r'equipments', EquipmentViewSet)
router.register(r'softwares', SoftwareViewSet)
router.register(r'purchases', PerchaseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
