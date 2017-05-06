from rest_framework import serializers
from .models import Hospital,Patient

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('HospitalId','Name','Contact','Address','Specialization','Distance')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('UID','Name','Age','AgeGroup','HospitalId')