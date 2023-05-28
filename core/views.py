from django.shortcuts import render, redirect
from .models import *
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import braintree


# Configure Braintree
braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    merchant_id=settings.BRAINTREE_MERCHANT_ID,
    public_key=settings.BRAINTREE_PUBLIC_KEY,
    private_key=settings.BRAINTREE_PRIVATE_KEY
)



def home(request):
    types = Type.objects.all()
    return render(request, 'home.html', {'types': types})


def attraction_list(request, type_id):
    type = Type.objects.get(id=type_id)
    attractions = Attraction.objects.filter(type=type)

    context = {
            'attractions': attractions,
            'type':type
    }
    return render(request, 'attraction_list.html', context)


def attraction_detail(request, attraction_id):
    attraction = Attraction.objects.get(id=attraction_id)
    hotels = Hotel.objects.filter(attraction_id=attraction_id)
    tour_operators = TourOperator.objects.filter(attraction_id=attraction_id)
    interesting_facts = InterestingFacts.objects.filter(attraction_id=attraction_id)

    context = {
        'attraction': attraction, 
        'hotels': hotels, 
        'tour_operators': tour_operators,
        'interesting_facts':interesting_facts
    }
    return render(request, 'attraction_detail.html', context)


def hotel_detail(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)

    context = {
        'hotel':hotel
    }

    return render(request, 'hotel_detail.html', context)


def operator_detail(request, operator_id):
    operator = TourOperator.objects.get(id=operator_id)
    email_to = operator.email

    message_name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    ctx = {
        'message_name': message_name,
        'email': email,
        'subject': subject,
        'message': message
    }
    message = render_to_string('email.html',ctx)

    if request.method == 'POST' and email and message:
        send_mail(email, 
        message, 
        settings.EMAIL_HOST_USER, 
        [email_to], 
        fail_silently=False, 
        html_message=message)

    context = {
        'operator':operator
    }

    return render(request, 'operator_detail.html', context)


def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        guest_name = request.POST['guest_name']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        
        # Create a new booking
        booking = Booking(room=room, guest_name=guest_name, check_in_date=check_in_date, check_out_date=check_out_date)
        booking.save()
        
        # Generate a client token for Braintree
        client_token = braintree.ClientToken.generate()

        return render(request, 'checkout.html', {'room': room, 'booking': booking, 'client_token': client_token})
    
    return render(request, 'book_room.html', {'room': room})


def process_payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    nonce = request.POST.get('payment_method_nonce', None)
    result = braintree.Transaction.sale({
        "amount": str(booking.room.price),
        "payment_method_nonce": nonce,
        "options": {
            "submit_for_settlement": True
        }
    })
    
    if result.is_success:
        # Payment successful
        booking.payment_status = True
        booking.save()
        return redirect('booking_success')
    else:
        # Payment failed
        return redirect('booking_failed')
    

def booking_success(request):
    return render(request, 'booking_success.html')


def booking_failed(request):
    return render(request, 'booking_failed.html')