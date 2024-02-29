from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from .models import Event, Event_Media, Sponsors, Faculty, Member
from .serializers import EventSerializer, EventMediaSerializer, SponsorsSerializer, FacultySerializer, MemberSerializer

# Views for Event model
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def event_list(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views for Event_Media model
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def event_media_list(request):
    if request.method == 'GET':
        event_media = Event_Media.objects.all()
        serializer = EventMediaSerializer(event_media, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EventMediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views for Sponsors model
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def sponsors_list(request):
    if request.method == 'GET':
        sponsors = Sponsors.objects.all()
        serializer = SponsorsSerializer(sponsors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SponsorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views for Faculty model
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def faculty_list(request):
    if request.method == 'GET':
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Views for Member model
@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def member_list(request):
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
