from django.shortcuts import render
from .models import Job, Worker
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .models import Job
from .serializers import JobSerializer, WorkerSerializer
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
