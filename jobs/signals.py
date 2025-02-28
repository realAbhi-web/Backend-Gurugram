from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Worker

@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created:
        Worker.objects.create(user=instance)
