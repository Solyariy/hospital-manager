from django.contrib.auth import get_user_model
from django.views import generic

from hospital.models import Patient


class PatientListView(generic.ListView):
    model = Patient
    # paginate_by = 5
    context_object_name = "patient_list"
    template_name = "patients/patient-list.html"


class PatientDetailView(generic.DetailView):
    model = Patient
    template_name = "patients/patient-detail.html"
