from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class MappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_date', 
                 'patient_details', 'doctor_details']
        read_only_fields = ['assigned_date']
        extra_kwargs = {
            'patient': {'write_only': True, 'required': True},
            'doctor': {'write_only': True, 'required': True},
        }