from django.shortcuts import render, redirect
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
