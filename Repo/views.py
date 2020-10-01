from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import DepartmentSerializer, LabSerializer, ComputerSerializer, SoftwareSerializer, PurchaseSerializer, EquipmentSerializer
from .models import Department, Lab, Computer, Software, Purchase, Equipment


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer


class labViewSet(viewsets.ModelViewSet):
    queryset = Lab.objects.all().order_by('id')
    serializer_class = LabSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all().order_by('id')
    serializer_class = ComputerSerializer


class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all().order_by('id')
    serializer_class = SoftwareSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('id')
    serializer_class = PurchaseSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all().order_by('id')
    serializer_class = EquipmentSerializer
