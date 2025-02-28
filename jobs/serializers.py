from rest_framework import serializers
from .models import Job, Worker
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    employer = serializers.IntegerField(write_only=True)  # Accepts raw user ID
    worker = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        employer_id = validated_data.pop("employer")  # Extract employer ID
        employer, _ = User.objects.get_or_create(id=employer_id, defaults={"username": f"user{employer_id}"})
        validated_data["employer"] = employer

        worker_id = validated_data.pop("worker", None)
        if worker_id:
            worker = Worker.objects.filter(id=worker_id).first()
            validated_data["worker"] = worker  # Set worker only if exists

        job = Job.objects.create(**validated_data)
        return job


class WorkerSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(write_only=True)  # Accepts raw user ID

    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        user_id = validated_data.pop("user")  # Extract user ID
        user, _ = User.objects.get_or_create(id=user_id, defaults={"username": f"user{user_id}"})
        validated_data["user"] = user  # Assign user object

        # ✅ Check if Worker exists, update if it does, otherwise create it
        worker, _ = Worker.objects.update_or_create(user=user, defaults=validated_data)
        return worker