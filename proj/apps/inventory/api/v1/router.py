
from rest_framework import routers
from .viewset import PersonListAPIView

router = routers.DefaultRouter()
router.register('persons', PersonListAPIView)
