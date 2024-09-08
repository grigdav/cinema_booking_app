from django.db import models
from django.contrib.auth.models import User

class CinemaRoom(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()  # Number of rows in the room
    seats_per_row = models.IntegerField()  # Number of seats per row

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')  # Store movie poster
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Schedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema_room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ('cinema_room', 'start_time')

    def __str__(self):
        return f'{self.movie.title} in {self.cinema_room.name} at {self.start_time}'

class Seat(models.Model):
    cinema_room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    seat_number = models.IntegerField()

    class Meta:
        unique_together = ('cinema_room', 'row_number', 'seat_number')

    def __str__(self):
        return f'Row {self.row_number}, Seat {self.seat_number} in {self.cinema_room.name}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('schedule', 'seat')

    def __str__(self):
        return f'Booking by {self.user.username} for {self.seat} during {self.schedule}'

    # Method to check if the seat is available during the movie
    @staticmethod
    def is_seat_available(schedule, seat):
        return not Booking.objects.filter(schedule=schedule, seat=seat).exists()

