from django.urls import path
from .views import job_list, job_detail, job_list_api, worker_list_api  # Remove home import (handled in project/urls.py)

urlpatterns = [
    path("", job_list, name="job_list"),  # Jobs listing at "/jobs/"
    path("<int:job_id>/", job_detail, name="job_detail"),  # Job details at "/jobs/1/"
    path('api/jobs/', job_list_api, name='job_list_api'),
     path("api/workers/", worker_list_api, name="worker_list_api"),
]
