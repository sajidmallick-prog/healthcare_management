from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated

class PatientListCreate(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()

class PatientUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        patient = get_object_or_404(Patient, id=id, user=request.user)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Patient updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        patient = get_object_or_404(Patient, id=id, user=request.user)
        patient.delete()
        return Response({'message': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)