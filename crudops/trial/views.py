from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Trial
from .serializer import TrialSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def trialList(request):
    trials = Trial.objects.all()
    serializer = TrialSerializer(trials, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def trailDetail(request,pk):
    trials = Trial.objects.get(id=pk)
    serializer = TrialSerializer(trials , many = False)
    return Response(serializer.data)

@api_view(['POST'])
def trialCreate(request,pk):
    trials = Trial.objects.get(id=pk)
    serializer = TrialSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def trialUpdate(request,pk):
    trials = Trial.objects.get(id=pk)
    serializer = TrialSerializer(instance = trials, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def trialDelete(request,pk):
    trials = Trial.objects.get(id=pk)
    trials.delete()

    return Response('Deleted')