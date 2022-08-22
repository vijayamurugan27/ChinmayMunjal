from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        # fields = ['url', 'username', 'email', 'is_staff', 'id', 'last_name', 'first_name', 'password','is_active' , 'is_superuser', 'last_login', 'date_joined' ]
        # fields = ['username', 'first_name', 'last_name', 'email', 'password', 'groups', 'user_permissions','is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined']
                                ### 'groups, 'user_permissions wont work in this fields, in the above line of code.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),    
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]