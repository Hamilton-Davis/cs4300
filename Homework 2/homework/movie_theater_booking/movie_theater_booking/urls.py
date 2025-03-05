"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet, base, movie_list, seat_booking, booking_history, book_seat, confirm_booking
from django.conf import settings

base_url = settings.FORCE_SCRIPT_NAME if settings.FORCE_SCRIPT_NAME else ''

# Setting up the API router
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include(router.urls)),
    
    # Base UI View
    path('', base, name='base'),

    # Template-based views
    path('movies/', movie_list, name='movie_list'),
    path('seats/', seat_booking, name='seat_booking'),
    path('bookings/', booking_history, name='booking_history'),

    # Booking-specific endpoints
    path('book_seat/<int:movie_id>/', book_seat, name='book_seat'),
    path('confirm_booking/<int:movie_id>/<int:seat_id>/', confirm_booking, name='confirm_booking'),
]

