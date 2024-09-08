import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import CinemaRoom, Schedule, Seat, Booking

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CinemaRoomListView(View):
    """
    Displays a list of cinema rooms
    """
    def get(self, request):
        rooms = CinemaRoom.objects.all()
        return render(request, 'room_list.html', {'rooms': rooms})

class MovieListView(View):
    """
    Displays a list of movies showing in a specific cinema room.
    """
    def get(self, request, room_id):
        cinema_room = get_object_or_404(CinemaRoom, id=room_id)
        schedules = Schedule.objects.filter(cinema_room=cinema_room).select_related('movie')
        
        return render(request, 'movie_list.html', {
            'cinema_room': cinema_room,
            'schedules': schedules  # Pass Schedule objects instead of just movies
        })


class SeatSelectionView(View):
    """
    Displays available and unavailable seats for the selected movie and handles seat booking
    """
    def get(self, request, schedule_id):
        schedule = get_object_or_404(Schedule, id=schedule_id)
        room = schedule.cinema_room
        seats = Seat.objects.filter(cinema_room=room)

        # Check availability for each seat
        seat_status = []
        for seat in seats:
            is_booked = Booking.objects.filter(schedule=schedule, seat=seat).exists()
            seat_status.append({
                'seat': seat,
                'is_booked': is_booked
            })

        return render(request, 'seat_selection.html', {
            'schedule': schedule,
            'seat_status': seat_status
        })

    @method_decorator(csrf_exempt)  # CSRF exempt for simplicity (only in dev)
    def post(self, request, schedule_id):
        seat_id = request.POST.get('seat_id')
        schedule = get_object_or_404(Schedule, id=schedule_id)
        seat = get_object_or_404(Seat, id=seat_id)

        # Check if the seat is already booked
        if Booking.objects.filter(schedule=schedule, seat=seat).exists():
            return JsonResponse({'status': 'error', 'message': 'Seat already booked'}, status=400)

        # Create a booking
        Booking.objects.create(
            user=request.user,  # Assuming the user is logged in
            schedule=schedule,
            seat=seat,
            booking_time=datetime.datetime.now()
        )

        return JsonResponse({'status': 'success', 'message': 'Seat booked successfully', 'seat_id': seat_id})
