from django.contrib import admin
from django.urls import path, include
from jobs.views import home  # Import `home` view from jobs app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # Homepage at "/"
    path("jobs/", include("jobs.urls")),  # Jobs app handles "/jobs/"
]
