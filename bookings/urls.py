from django.urls import path
from . import views  # Импортируем представления из текущего приложения

urlpatterns = [
    path('', views.computer_list, name='computer_list'),  # Список компьютеров
    path('book/<int:computer_id>/', views.book_computer, name='book_computer'),  # Бронирование
]