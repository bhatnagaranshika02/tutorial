from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import permissions,viewsets
from tutorials.quickstart.serializers import UserSerializer,GroupSerializer

class UserViewSets(viewset.ModelViewSets):
	queryset=User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAuthenticated]

class GroupViewSets(viewset.ModelViewSets):
	queryset=Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAuthenticated]