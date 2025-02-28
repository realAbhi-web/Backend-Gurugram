from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Job, Worker, Profile, Contractor
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import Job
from .serializers import JobSerializer, WorkerSerializer, ProfileSerializer, ContractorSerializer
from rest_framework import status


def job_list(request):
    jobs = Job.objects.all()  # Fetch all jobs
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)  # Fetch a single job by ID
    return render(request, 'jobs/job_detail.html', {'job': job})

def home(request):
    return HttpResponse("<h1>Welcome to Job Platform!</h1>")

@api_view(['GET','POST'])
def job_list_api(request):
    if request.method=='GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def worker_list_api(request):
    if request.method=='GET':
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # ✅ Handle worker creation
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST', 'GET'])
def register_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')  # "user" or "contractor"
        skills = request.data.get('skills')
        hourly_rate = request.data.get('hourly_rate')
        location = request.data.get('location')

        if not username or not password or not role:
            return Response({"error": "Username, password, and role are required."}, status=status.HTTP_400_BAD_REQUEST)

        if role not in ['user', 'contractor']:
            return Response({"error": "Invalid role. Choose 'user' or 'contractor'."}, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Check if user already exists
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role)

        if role == 'contractor':
            if not skills or not hourly_rate or not location:
                return Response({"error": "Contractors must provide skills, hourly rate, and location."},
                                status=status.HTTP_400_BAD_REQUEST)
            Contractor.objects.create(user=user, skills=skills, hourly_rate=hourly_rate, location=location)

        return Response({"message": f"User {username} registered as {role}."}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_all_users(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_contractors(request):
    contractors = Contractor.objects.all()
    serializer = ContractorSerializer(contractors, many=True)
    return Response(serializer.data)


