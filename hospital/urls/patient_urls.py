from django.urls import path
from hospital.views.patient_views import PatientListView, PatientDetailView

urlpatterns = [
    path("", PatientListView.as_view(), name="list"),
    path("<int:pk>/", PatientDetailView.as_view(), name="detail")
]

app_name = "patients"
