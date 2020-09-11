from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DepartmentSerializer, LabSerializer
from .models import Department, Lab


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer


class labViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all().order_by('id')
    serializer_class = LabSerializer
