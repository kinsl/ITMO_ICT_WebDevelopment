from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import RegistrationForm, FeedbackForm
from .models import Flight, Booking


def register_request(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались!")
            return redirect("view_flights")
        messages.error(request, "Регистрация не удалась. Проверьте введённые данные.")
    else:
        form = RegistrationForm()
    return render(request=request, template_name="flights/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"Вы вошли как {user.last_name} {user.first_name}.")
                return redirect("view_flights")
            else:
                messages.error(request, "Неверный логин или пароль.")
        else:
            messages.error(request, "Неверный логин или пароль.")
    form = AuthenticationForm()
    return render(request=request, template_name="flights/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Вы успешно вышли.")
    return redirect("login")


@login_required
def view_flights(request):
    flights = Flight.objects.exclude(bookings__user=request.user).filter(date__gt=timezone.now()).order_by("date")
    return render(request, "flights/flights_list.html", {"flights": flights})


@login_required
def view_bookings(request, tab):
    if tab == "upcoming":
        bookings = Booking.objects.filter(user=request.user, flight__date__gte=timezone.now())
    else:
        bookings = Booking.objects.filter(user=request.user, flight__date__lt=timezone.now())

    return render(request, "flights/my_flights.html", {"bookings": bookings, "active_tab": tab})


@login_required
def book_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    Booking.objects.create(user=request.user, flight=flight)
    messages.success(request, "Рейс успешно забронирован!")
    return redirect("view_flights")


@login_required
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, "Бронь успешно отменена!")
    return redirect("view_bookings", "upcoming")


@login_required
def give_feedback(request, flight_id):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.flight = Flight.objects.get(id=flight_id)
            feedback.save()
            messages.success(request, "Ваш отзыв успешно отправлен!")
            return redirect("view_bookings", "past")
    else:
        form = FeedbackForm()
    return render(request, "flights/feedback.html", {"form": form})


@login_required
def flight_details(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, "flights/flight_details.html", {"flight": flight})
