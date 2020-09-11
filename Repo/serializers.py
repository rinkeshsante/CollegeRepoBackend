from rest_framework import serializers

from .models import Department, Computer, Equipment, Lab, Software, Perchase

# this page will be used to decide the fields in api json


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class LabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lab
        fields = ('id', 'name', 'code', 'lab_number')


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Computer
        fields = ('id', 'name', 'Computer_no', 'ram', 'storage')


class EquipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'name', 'equipment_no', 'code')


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = ('id', 'name', 'code', 'software_no')


class PerchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perchase
        fields = ('id', 'bill_no', 'supplier', 'rate')
