from django.contrib.auth import get_user_model
from django.views import generic


class WorkerListView(generic.ListView):
    model = get_user_model()
    # paginate_by = 5
    context_object_name = "worker_list"
    template_name = "workers/worker-list.html"


class WorkerDetailView(generic.DetailView):
    model = get_user_model()
    template_name = "workers/worker-detail.html"
