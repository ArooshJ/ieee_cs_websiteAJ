from django.urls import path
from .views import (
    event_list, event_media_list, sponsors_list, faculty_list, member_list
)

urlpatterns = [
    path('events/', event_list, name='event-list'),
    path('event-media/', event_media_list, name='event-media-list'),
    path('sponsors/', sponsors_list, name='sponsors-list'),
    path('faculty/', faculty_list, name='faculty-list'),
    path('members/', member_list, name='member-list'),
]