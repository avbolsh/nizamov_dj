from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CustomUserSerilizer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerilizer
    permission_classes = [permissions.IsAdminUser]
