from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntryExitRecordViewSet

router = DefaultRouter()
router.register(r'entryexitrecords', EntryExitRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]