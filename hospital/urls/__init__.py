from django.urls import path, include
from . import workers

urlpatterns = [
    path("", include("hospital.urls.base", namespace="base")),
    path("workers/", include("hospital.urls.workers", namespace="workers")),
    path("patients/", include("hospital.urls.patients", namespace="patients")),
    path("tasks/", include("hospital.urls.tasks", namespace="tasks"))
]

app_name = "hospital"
