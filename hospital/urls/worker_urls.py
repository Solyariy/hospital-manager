from django.urls import path
from hospital.views.worker_views import WorkerListView, WorkerDetailView

urlpatterns = [
    path("", WorkerListView.as_view(), name="list"),
    path("<int:pk>/", WorkerDetailView.as_view(), name="detail")
]

app_name = "workers"
