from django.urls import path
from .views import CinemaRoomListView, MovieListView, SeatSelectionView

urlpatterns = [
    path('', CinemaRoomListView.as_view(), name='cinema_room_list'),
    path('room/<int:room_id>/', MovieListView.as_view(), name='movie_list'),
    path('schedule/<int:schedule_id>/seats/', SeatSelectionView.as_view(), name='seat_selection'),
]

