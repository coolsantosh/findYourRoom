from django.urls import path
from api.views import RoomListView

urlpatterns = [
    path('room/',RoomListView.as_view(),name="room-list"),
]