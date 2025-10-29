from rest_framework import generics, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.settings import api_settings

from users.models import User
from users.serializers import UserSerializer, AuthTokenSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = (IsAdminUser,)


class CreateUserView(generics.CreateAPIView):
   serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
   serializer_class = AuthTokenSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
   serializer_class = UserSerializer
   permission_classes = (IsAuthenticated,)

   def get_object(self):
      return self.request.user
