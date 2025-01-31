from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Computer, Booking
from .forms import BookingForm

def computer_list(request):
    computers = Computer.objects.filter(is_available=True)
    return render(request, 'bookings/computer_list.html', {'computers': computers})

def book_computer(request, computer_id):
    computer = Computer.objects.get(id=computer_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.computer = computer
            booking.save()
            return redirect('computer_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_computer.html', {'form': form, 'computer': computer})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})