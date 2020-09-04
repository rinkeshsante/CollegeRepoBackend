from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DepartmentSerializer
from .models import Department


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
