from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics,  status
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated

class DoctorListCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class DoctorUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        doctor = get_object_or_404(Doctor, id=id)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Doctor updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DoctorDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        doctor = get_object_or_404(Doctor, id=id)
        doctor.delete()
        return Response({'message': 'Doctor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
