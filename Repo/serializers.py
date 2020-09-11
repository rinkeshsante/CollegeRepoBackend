from rest_framework import serializers

from .models import Department, Computer, Equipment, Lab, Software


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class LabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lab
        fields = ('id', 'name', 'department')
