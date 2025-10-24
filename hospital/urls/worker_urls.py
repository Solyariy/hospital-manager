from django.urls import path

from hospital.views import base


urlpatterns = [
    path("", base.index, name="index")
]
