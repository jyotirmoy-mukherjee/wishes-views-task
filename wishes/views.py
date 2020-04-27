from wishes.models import Wish
from wishes.serializers import WishSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

#WishList class definition here
class WishList():
    pass

#WishDetail class definition here
class WishDetail():
    pass

class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer