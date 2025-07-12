from django.urls import path
from .views import PatientListCreate, PatientDetail, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('patients/', PatientListCreate.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetail.as_view(), name='patient-detail'),
    path('patients/update/<int:id>/', PatientUpdateView.as_view(), name='patient-update'),
    path('patients/delete/<int:id>/', PatientDeleteView.as_view(), name='patient-delete'),
]
