from django.urls import path
from .views import MappingListCreate, MappingListByPatient, MappingDetail

urlpatterns = [
    # POST /api/mappings/ - Assign a doctor to a patient
    # GET /api/mappings/ - Retrieve all patient-doctor mappings
    path('', MappingListCreate.as_view(), name='mapping-list'),
    
    # GET /api/mappings/<patient_id>/ - Get doctors for specific patient
    path('<int:patient_id>/', MappingListByPatient.as_view(), name='mapping-by-patient'),
    
    # DELETE /api/mappings/<id>/ - Remove a doctor from a patient
    path('<int:id>/', MappingDetail.as_view(), name='mapping-detail'),
]