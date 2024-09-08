from django.contrib import admin
from .models import CinemaRoom, Movie, Schedule, Seat, Booking

@admin.register(CinemaRoom)
class CinemaRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows', 'seats_per_row')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','duration')
    search_fields = ('title',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'cinema_room', 'start_time', 'end_time')
    list_filter = ('cinema_room', 'start_time', 'movie')
    search_fields = ('movie__title', 'cinema_room__name')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('cinema_room', 'row_number', 'seat_number')
    list_filter = ('cinema_room',)
    search_fields = ('cinema_room__name', 'row_number', 'seat_number')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'schedule', 'seat', 'booking_time')
    list_filter = ('schedule__cinema_room', 'booking_time')
    search_fields = ('user__username', 'schedule__movie__title', 'seat__cinema_room__name')

