from rest_framework import serializers
from .models import Event, Event_Media, Sponsors, Faculty, Member

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_Media
        fields = '__all__'

class SponsorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsors
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
