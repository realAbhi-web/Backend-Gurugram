from django.db import models
from django.contrib.auth.models import User

class Worker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Links to Django’s built-in User model
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255)  # Example: "Python, Django, JavaScript"
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='worker_profiles/', blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_jobs")  # Employer who posted
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_jobs")  # Assigned worker
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
