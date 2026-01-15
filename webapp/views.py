import random

from django.shortcuts import render, redirect
from Backend.models import roomnamedb, roomtypedb, staffdb
from webapp.models import customercontactdb, bookingdb, Registerdb, Totaldb
from django.contrib import messages
import razorpay


# Create your views here.
def home_page(request):
    cat = roomtypedb.objects.all()
    return render(request, "1home.html", {'cat': cat})


def about_page(request):
    cat = staffdb.objects.all()
    return render(request, "2about.html", {'cat': cat})


def services_page(request):
    return render(request, "3services.html")


def rooms_page(request):
    return render(request, "4rooms.html")


def customer_contact_page(request):
    return render(request, "5contact.html")


def save_customer_contact_page(request):
    if request.method == "POST":
        na = request.POST.get('cname')
        em = request.POST.get('cemail')
        cn = request.POST.get('cnumber')
        cs = request.POST.get('csubject')
        cm = request.POST.get('cmessage')
        obj = customercontactdb(CONTACTNAME=na, CONTACTEMAIL=em, CONTACTNUMBER=cn, CONTACTSUBJECT=cs, CONTACTMESSAGE=cm)
        obj.save()
        messages.success(request, "Message Send successfully")
        return redirect(customer_contact_page)


# for getting specific roomsname(roomnumber1,roomnumber2)  inherited from roomtype(luxury,specific,lowclass)
# Backend models(roomnamedb) connected to Webapp  page and showing  someparticular category added to luxury type like wise..

def filtered_room_name(request, room_name):
    data = roomnamedb.objects.filter(ROOMTYPE=room_name)
    return render(request, "6roomname_filtered.html", {'data': data})


def save_room_page(request):
    return render(request, "7savedroom.html")


def booking_page(request, pro_id):
    data = bookingdb.objects.filter(CUSTOMERNAME=request.session['USERNAME'])
    cat = roomnamedb.objects.get(id=pro_id)
    return render(request, "7booking.html", {'cat': cat, 'data': data})


def save_room_page(request):
    global total
    data = bookingdb.objects.filter(CUSTOMERNAME=request.session['USERNAME'])
    subtotal = 0
    tax = 100
    total = 0

    for d in data:
        subtotal = subtotal + d.TOTALPRICE
        if subtotal > 5000:
            tax = 10
        else:
            tax = 20
        total = subtotal + tax

    return render(request, "7savedroom.html", {'data': data, 'subtotal': subtotal, 'total': total, 'tax': tax})


def save_roompages_input(request):
    if request.method == "POST":
        na = request.POST.get('customername')
        mb = request.POST.get('customermobile')  # Now CharField, no conversion needed
        tl = request.POST.get('totalprice')
        
        # Optionally link to the last booking made by this customer
        last_booking = None
        if 'USERNAME' in request.session:
            last_booking = bookingdb.objects.filter(
                CUSTOMERNAME=request.session['USERNAME']
            ).order_by('-id').first()
        
        obj = Totaldb(
            BOOKING=last_booking,
            CUSTOMERNAME=na, 
            MOBILE=mb,  # Now CharField
            TOTALPRICE=int(tl) if tl else None
        )
        obj.save()
        return redirect(payment_page)


def delete_item(request, pro_id):
    x = bookingdb.objects.filter(id=pro_id)
    x.delete()
    messages.warning(request, "Room deleted successfully")
    return redirect(save_room_page)


def save_booking_page(request, CONTACTEMAIL=None):
    if request.method == "POST":
        na = request.POST.get('bname')
        em = request.POST.get('bemail')
        chn = request.POST.get('bcheckin')
        cho = request.POST.get('bcheckout')
        ta = request.POST.get('btotaladults')
        tc = request.POST.get('btotalchilds')
        sr_id = request.POST.get('bselectroom')  # This is now the room ID
        sre = request.POST.get('bspecialrequest')
        tp = request.POST.get('btotalprice')

        # obj = bookingdb(CUSTOMERNAME=na, CONTACTEMAIL=em, CHECKIN=chn, CHECKOUT=cho, TOTALADULTS=ta, TOTALCHILDS=tc,
        #                 SELECTROOM=sr, SPECIALREQUEST=sre, TOTALPRICE=tp)
        # # Check for overlapping bookings
        # overlapping_bookings = bookingdb.objects.filter(
        #     SELECTROOM=sr,
        #     CHECKIN=chn,
        #     CHECKOUT=cho
        # )
        #
        # if overlapping_bookings.exists():
        #     messages.error(request, "The selected room is already booked for the specified dates.")
        #     return redirect('save_room_page')  # Redirect back to the booking form page
        #
        # # If no overlap, save the booking
        #
        # messages.success(request, "saved room successfully")
        #
        #
        #
        # obj.save()
        #
        # messages.success(request, "Room booked successfully.")
        # subject = "Conragatulations roombooked"
        # message = f"Dear customer you have booked a room succesfully :   Thank you "
        # send_mail(subject, message, EMAIL_HOST_USER, [obj.CONTACTEMAIL], fail_silently=True, )
        #
        # return redirect(save_room_page)
        # Get the room object from the ID
        try:
            room_obj = roomnamedb.objects.get(id=sr_id)
        except roomnamedb.DoesNotExist:
            messages.error(request, "Invalid room selection.")
            return redirect('save_room_page')
        
        # Check for overlapping bookings with the ForeignKey and DateField
        overlapping_bookings = bookingdb.objects.filter(
            SELECTROOM=room_obj
        ).filter(
            CHECKIN__lte=cho,
            CHECKOUT__gte=chn
        )

        if overlapping_bookings.exists():
            messages.error(request, "The selected room is already booked for the specified dates.")
            return redirect('save_room_page')  # Redirect back to the booking form page
        else:
            # Get the customer if logged in
            customer_obj = None
            if 'USERNAME' in request.session:
                try:
                    customer_obj = Registerdb.objects.get(USERNAME=request.session['USERNAME'])
                except Registerdb.DoesNotExist:
                    pass

            # If no overlap, save the booking
            obj = bookingdb(
                CUSTOMER=customer_obj,
                CUSTOMERNAME=na,
                CONTACTEMAIL=em,
                CHECKIN=chn,
                CHECKOUT=cho,
                TOTALADULTS=int(ta) if ta else None,
                TOTALCHILDS=int(tc) if tc else None,
                SELECTROOM=room_obj,  # Now a ForeignKey
                SPECIALREQUEST=sre,
                TOTALPRICE=int(tp) if tp else None
            )
            obj.save()

            messages.success(request, "Room booked successfully.")

            # Send confirmation email
            subject = "Congratulations roombooked"
            message = f"Dear customer you have booked a room succesfully :   Thank you & have a nice day ,Hoteliers"
            send_mail(subject, message, EMAIL_HOST_USER, [obj.CONTACTEMAIL], fail_silently=True, )
            return redirect('save_room_page')


        return redirect('save_room_page')  # If not POST, just redirect

def rooms_pages_new(request):
    cat = roomtypedb.objects.all()
    return render(request, "8onlyroom.html", {'cat': cat})


def ourteam_page(request):
    cat = staffdb.objects.all()
    return render(request, "9ourteam.html", {'cat': cat})


def testimonial_page(request):
    return render(request, "10testimonial.html")


# login_page
def signup_page(request):
    return render(request, "11signup.html")


def signin_page(request):
    return render(request, "12userlogin.html")


# saving password,confirmpassword to database from signup_page
def save_user(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        obj = Registerdb(USERNAME=na, EMAIL=em, PASSWORD=p1, CONFIRMPASSWORD=p2)
        obj.save()
        messages.success(request, "signup successfully")
        return redirect(signin_page)


def user_login_page(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pswd = request.POST.get('upassword')
        if Registerdb.objects.filter(USERNAME=un, PASSWORD=pswd).exists():
            request.session['USERNAME'] = un
            request.session['PASSWORD'] = pswd
            messages.success(request, "signin successfully")
            return redirect(home_page)

        else:
            messages.warning(request, "signin failed")
            return redirect(signin_page)
    else:
        return redirect(signin_page)

    # for deleteing session userlogout


def userlogout_page(request):
    del request.session['USERNAME']
    del request.session['PASSWORD']
    messages.success(request, "signout successfully")
    return redirect(home_page)


# for payment
def payment_page(request):
    customer = Totaldb.objects.order_by('-id').first()
    payy = customer.TOTALPRICE
    amount = int(payy * 100)
    payy_str = str(amount)
    for i in payy_str:
        print(i)
    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_klfWwvjaFXjXmC', 's9P7dwOwYckK352FfRJOXIRV'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})

    return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str})


from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


def generate_pdf(request):
    # Data to pass to the template
    username = request.session.get('USERNAME', 'Guest')

    # Render the template with context
    context = {
        'username': username,
        'data': 'Your data here',
    }

    # Render the HTML template with context data
    html_string = render_to_string('your_template.html', context)

    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(html_string, dest=response)

    # Return the response
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html_string + '</pre>')
    return response


from django.core.mail import send_mail
from django.core.mail import EmailMessage
from Hotelierss.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage







 #for generating otp starts here
def generate_otp(request):
     otp=random.randint(10000,55555)
     return(otp)
def reset_password_email_verification_page(request):
    return render(request,"15password_reset_email.html")


def reset_password_email_verification(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Registerdb.objects.filter(EMAIL=email).exists():
            user = Registerdb.objects.get(EMAIL=email)
            u_otp = generate_otp(request)
            request.session['otp'] = u_otp
            subject = "Forgot Password"
            message = f"Dear user OTP for reset your account password is : {u_otp}   Thank you , Hoteliers"
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently=True, )  # send otp to mail
            context = {
                'message': "An OTP sent to your registered email id.",
                'user': user,
            }
            return render(request, "16password_reset_otp.html", context)
        else:
            return render(request, "15password_reset_otp.html", {'error': "Sorry..Invalid email id"})
    else:
        return redirect("home")

def passwordReset_verify_otp(request,user_id):
    user = Registerdb.objects.get(id=user_id)
    if request.method == "POST":
        u_otp = str(request.POST.get('otp')).strip() #removing unwanted space for the otp, if we copy paste the progra,m
        s_otp = str(request.session.get('otp')).strip() # get stored otp
        if u_otp == s_otp:  # verifying two otp
            context = {
                'user': user
            }
            return render(request, "17reset_password.html", context)
        else:
            context = {
                'error': "OTP does not match.!!",
                'user': user,
            }
            return render(request, "16password_reset_otp.html", context)
    else:
        return redirect("user_login_page")

from django.contrib.auth.hashers import make_password
def reset_password(request, username):
    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = Registerdb.objects.get(USERNAME=username)
                Registerdb.objects.filter(USERNAME=username).update(PASSWORD=password1)
                messages.success(request, "Your password has been reset successfully! "
                                          "You can now log in with your new password.")
                subject = "Password Changed"
                message = f"Dear user, your password has been recently changed. Thank you, Team t4Text"
                send_mail(subject, message, EMAIL_HOST_USER, [user.EMAIL],
                          fail_silently=True)  # Send email notification
                messages.success(request, "Reset password successfully")
                return redirect("user_login_page")
            except Registerdb.DoesNotExist:
                messages.error(request, "User not found.")
                return redirect("reset_password", USERNAME=username)
        else:
            return render(request, "17reset_password.html",
                          {'error': "Sorry, passwords do not match!", 'user': username})
    else:
        return redirect("home")