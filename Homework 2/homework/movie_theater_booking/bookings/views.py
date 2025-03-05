from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# API ViewSets (for RESTful API endpoints)
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Template-based Views
def base(request):
    return render(request, 'bookings/base.html')

def movie_list(request):
    """Displays a list of available movies."""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def booking_history(request):
    """Shows the booking history."""
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def book_seat(request, movie_id):
    """Shows seat selection for a specific movie."""
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(booking_status='available')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def seat_booking(request):
    seats = Seat.objects.filter(is_booked=False)  # Use 'is_booked' instead of 'booking_status'
    return render(request, 'bookings/seat_booking.html', {'seats': seats})


def confirm_booking(request, movie_id, seat_id):
    """Confirms the booking of a seat."""
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)

    if request.method == 'POST':
        # Requires user authentication (Not implemented yet)
        Booking.objects.create(movie=movie, seat=seat, user=request.user, show_time='19:00')
        seat.booking_status = 'booked'
        seat.save()
        return redirect('booking_history')

    return render(request, 'bookings/confirm_booking.html', {'movie': movie, 'seat': seat})


