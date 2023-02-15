from rest_framework import serializers
from .models import Drone,Medication, Loads

class DronesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ['serial_number','model','weight_limit', 'battery_capacity','state']




class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['name', 'weight','code', 'image']


class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loads
        fields = ['drone','medication']


class BSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ['battery_capacity']