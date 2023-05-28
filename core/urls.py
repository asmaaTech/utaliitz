from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('type/<int:type_id>/', views.attraction_list, name='attraction_list'),
    path('hotel/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('book_room/<int:room_id>/', views.book_room, name='book_room'),
    path('process_payment/<int:booking_id>/', views.process_payment, name='process_payment'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('booking_failed/', views.booking_failed, name='booking_failed'),
    path('operator/<int:operator_id>/', views.operator_detail, name='operator_detail'),
    path('attraction/<int:attraction_id>/', views.attraction_detail, name='attraction_detail'),
    
]