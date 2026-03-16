from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from user.serializers import UserSerializer


class UserRegisterView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
