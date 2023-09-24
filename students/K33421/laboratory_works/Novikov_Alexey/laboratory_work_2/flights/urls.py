"""
URL configuration for simple_django_web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_flights, name="view_flights"),
    path("my/<str:tab>/", views.view_bookings, name="view_bookings"),
    path("flight/<int:flight_id>/book/", views.book_flight, name="book_flight"),
    path("booking/<int:booking_id>/delete/", views.delete_booking, name="delete_booking"),
    path("flight/<int:flight_id>/feedback/", views.give_feedback, name="give_feedback"),
    path("flight/<int:flight_id>/", views.flight_details, name="flight_details"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
]