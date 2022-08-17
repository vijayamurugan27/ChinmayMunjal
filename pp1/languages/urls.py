from xml.etree.ElementInclude import include
from django.urls import path, include

from languages import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', views.LanguageView)

urlpatterns = [
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # for authentication
]
