from django.urls import path
from .views import DoctorListCreate, DoctorDetail, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path('', DoctorListCreate.as_view(), name='doctor-list-create'),
    path('<int:id>/', DoctorDetail.as_view(), name='doctor-detail'),

    path('doctors/update/<int:id>/', DoctorUpdateView.as_view(), name='doctor-update'),
    path('doctors/delete/<int:id>/', DoctorDeleteView.as_view(), name='doctor-delete'),
]