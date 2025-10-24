from . import worker_urls

urlpatterns = [
    *worker_urls.urlpatterns
]

app_name = "hospital"