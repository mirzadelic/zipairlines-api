from django.urls import path, include
from rest_framework import routers

from .views import AirlineView


router = routers.DefaultRouter()

app_name = 'airlines'
urlpatterns = [
    path('', include(router.urls)),
    path('airplanes/', AirlineView.as_view(), name='airplane')
]
