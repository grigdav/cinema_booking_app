# cinema/management/commands/populate_db.py

from django.core.management.base import BaseCommand
from CinemaApp.models import CinemaRoom, Movie, Schedule, Seat
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Create cinema rooms
        rooms = ['Red', 'Blue', 'Green']
        for room_name in rooms:
            CinemaRoom.objects.get_or_create(name=room_name, rows=8, seats_per_row=10)
        
        # Create movies
        movies = [
                {'title': 'Avengers', 'duration': 120, 'poster': 'posters/poster1.jpg'},
                {'title': 'The Godfather', 'duration': 90, 'poster': 'posters/poster2.jpg'},
                {'title': 'The Dark Knight', 'duration': 150, 'poster': 'posters/poster3.jpg' },
                {'title': 'The Lord of the Rings', 'duration': 180, 'poster':'posters/poster4.jpg'}
        ]
        for movie_data in movies:
            Movie.objects.get_or_create(title=movie_data['title'], duration=movie_data['duration'])
        
        # Get all cinema rooms and movies
        rooms = CinemaRoom.objects.all()
        movies = Movie.objects.all()

                        # Create schedules and seats
        for room in rooms:
            for movie in movies:
                for _ in range(3):  # Example: 3 different show times
                    start_time = timezone.now() + timedelta(days=random.randint(1, 10))  # Random day between 1 and 10
                    end_time = start_time + timedelta(minutes=random.randint(60, 180))  # Random duration between 60 and 180 minutes
                    
                    Schedule.objects.get_or_create(
                        cinema_room=room,
                        movie=movie,
                        start_time=start_time,
                        end_time=end_time
                    )

                for row in range(1, 11):  # 10 rows
                    for seat_num in range(1, 9):  # 8 seats per row
                        Seat.objects.get_or_create(
                            cinema_room=room,
                            row_number=row,
                            seat_number=seat_num
                        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with initial data'))

