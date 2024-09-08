# Cinema Booking Application

This project is a cinema booking system built with Django. It allows users to browse available cinema rooms, view the movies playing in those rooms, and book specific seats for each movie. The system ensures that once a seat is booked, it becomes unavailable for the duration of the movie's screening.


## Project run on http://rsh2.itrm.ru/ 

You can enter site and test it. If you want to admin site enter http://rsh2.itrm.ru/admin 
- **Username** : cinema_admin
- **Password** : 1234

## Features

- **Cinema Room Management**: Multiple cinema rooms (e.g., Red, Blue, Green) with different seating arrangements.
- **Movie Scheduling**: Each cinema room can have multiple movies scheduled at different times, and each movie has its own poster and duration.
- **Seat Booking**: Users can view the available seats for a selected movie in a room and book any available seat. Booked seats are marked as unavailable and cannot be booked again for that movie.
- **Real-Time Updates**: Booked seats update dynamically on the seat selection page, ensuring accurate availability.

## Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL (with Docker support)
- **Frontend**: HTML5, CSS, JavaScript (Bootstrap for styling)
- **Deployment**: Docker for containerization

---

## Project Setup

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.7+
- PostgreSQL (or use Docker for the database setup)
- Docker and Docker Compose (for containerized setup)

### 1. Clone the Repository

First, clone the project repository to your local machine:

```bash
git@github.com:grigdav/cinema_booking_app.git
cd cinema_booking_app
```

### 2. Build and Run the Project with Docker

Docker Setup
For a complete Docker-based setup, follow these steps:

Build and run the Docker containers:
```
docker-compose up --build
```

The application will be running at http://localhost:8000, and the PostgreSQL database will run in a separate container.

To stop the containers, use:
```
docker-compose down
```

## 2.1 Run migrations (in another terminal window):
```
docker-compose exec web python manage.py migrate
```

## 2.2 Create a superuser (optional, for admin panel access):
```
docker-compose exec web python manage.py createsuperuser
```

## 2.3 Filling database mock data (optional):
```
docker-compose exec web python manage.py createsuperuser
```

### 3. Database Schema

The application uses the following database schema, which supports room management, movie scheduling, and seat bookings:

## Models

# CinemaRoom
Represents each cinema room. Each room can show different movies and has specific seating arrangements.

id: Primary key.
name: The name of the cinema room (e.g., "Red Room").
total_rows: The total number of seating rows in the room.
seats_per_row: The number of seats per row.

# Movie
Stores information about each movie being shown.

id: Primary key.
title: The name of the movie.
poster: A URL or file path to the movie's poster image.
duration: The duration of the movie in minutes.

# Schedule
Tracks when and where each movie is shown. Each schedule is linked to a specific Movie and CinemaRoom.

id: Primary key.
cinema_room: Foreign key to CinemaRoom.
movie: Foreign key to Movie.
start_time: The scheduled start time of the movie.
end_time: The scheduled end time of the movie (calculated from the movie duration).

# Seat
Represents each seat in a cinema room.

id: Primary key.
cinema_room: Foreign key to CinemaRoom.
row: The row number of the seat.
seat_number: The seat number within the row.
is_available: Boolean field that tracks whether the seat is available for booking.

# Booking
Tracks each booking made by a user for a specific movie and seat.

id: Primary key.
schedule: Foreign key to Schedule.
seat: Foreign key to Seat.
user: Foreign key to the user who made the booking.
booking_time: The date and time when the booking was made.

# Relationships
A CinemaRoom has multiple Schedules.
A Schedule links a Movie to a CinemaRoom at a specific time.
Each Seat belongs to a CinemaRoom and is unique within that room.
A Booking links a user to a specific Seat for a given Schedule.
