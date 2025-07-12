from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from patients.models import Patient
from doctors.models import Doctor
from rest_framework.permissions import IsAuthenticated


class MappingListCreate(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Return all mappings where patient belongs to current user
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        patient_id = request.data.get('patient')
        doctor_id = request.data.get('doctor')
        
        try:
            # patient = Patient.objects.get(id=patient_id, user=request.user)
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response(
                {"error": "Patient not found or access denied"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return Response(
                {"error": "Doctor not found"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            return Response(
                {"error": "This doctor is already assigned to the patient"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        mapping = PatientDoctorMapping.objects.create(patient=patient, doctor=doctor)
        serializer = self.get_serializer(mapping)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MappingListByPatient(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        # Ensure patient belongs to current user
        return PatientDoctorMapping.objects.filter(
            patient__id=patient_id, 
            patient__user=self.request.user
        )

class MappingDetail(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'