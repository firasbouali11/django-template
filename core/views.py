from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser


# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        users = Profile.objects.filter(is_active=True, is_superuser=False)
        return users

    def create(self, request, *args, **kwargs):
        data = request.data
        user = Profile.objects.create_user(
            username=data["username"],
            email=data["email"]
        )
        user.set_password(data["password"])
        user.save()

        return Response(ProfileSerializer(user).data)

    def update(self, request, *args, **kwargs):
        data = request.data
        user = Profile.objects.get(pk=self.get_object().id)
        user.username = data["username"]
        user.email = data["email"]
        if "pbkdf2_sha256$" not in data["password"]:
            user.set_password(data["password"])
        user.save()
        return Response(ProfileSerializer(user).data)
