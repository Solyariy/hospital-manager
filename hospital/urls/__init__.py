from django.urls import path, include
from . import worker_urls, patient_urls, task_urls

urlpatterns = [
    path("", include("hospital.urls.base", namespace="base")),
    path("workers/", include("hospital.urls.worker_urls", namespace="workers")),
    path("patients/", include("hospital.urls.patient_urls", namespace="patients")),
    path("tasks/", include("hospital.urls.task_urls", namespace="tasks"))
]

app_name = "hospital"
