from django.shortcuts import render, redirect, get_object_or_404
from Guest.models import *
from Seller.models import *
from User.models import *


def Homepage(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata = tbl_user.objects.get(id=request.session['uid'])
    productdata = tbl_product.objects.all()
    return render(request, 'User/Homepage.html', {
        'data': userdata,
        'product': productdata
    })


def UserProfile(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata = tbl_user.objects.get(id=request.session['uid'])
    return render(request, 'User/UserProfile.html', {'data': userdata})


def UserEditProfile(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    userdata = tbl_user.objects.get(id=request.session['uid'])
    district_data = tbl_district.objects.all()

    if request.method == "POST":
        # Supports both txt_name and name forms
        name = request.POST.get('txt_name') or request.POST.get('name')
        email = request.POST.get('txt_email') or request.POST.get('email')
        contact = request.POST.get('txt_contact') or request.POST.get('contact')
        bio = request.POST.get('txt_bio') or request.POST.get('bio')
        place_id = request.POST.get('place')

        if name:
            userdata.user_name = name
        if email:
            userdata.user_email = email
        if contact:
            userdata.user_contact = contact
        if bio:
            userdata.user_bio = bio
        if place_id:
            userdata.place = tbl_place.objects.get(id=place_id)

        userdata.save()
        return redirect('User:UserProfile')
    else:
        place_data = []
        if userdata.place and userdata.place.district_id:
            place_data = tbl_place.objects.filter(district_id=userdata.place.district_id)
        return render(request, 'User/UserEditProfile.html', {
            'data': userdata,
            'district': district_data,
            'place': place_data
        })


def UserChangePassword(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    user = tbl_user.objects.get(id=request.session['uid'])

    if request.method == "POST":
        old_pass = request.POST.get("txt_old")
        new_pass = request.POST.get("txt_new")
        re_pass = request.POST.get("txt_re")

        if user.user_password == old_pass:
            if new_pass == re_pass:
                user.user_password = new_pass
                user.save()
                return render(request, "User/UserChangePassword.html", {
                    "msg": "Password Changed Successfully"
                })
            else:
                return render(request, "User/UserChangePassword.html", {
                    "msg": "New Passwords do not match"
                })
        else:
            return render(request, "User/UserChangePassword.html", {
                "msg": "Old Password Incorrect"
            })
    else:
        return render(request, "User/UserChangePassword.html")


# 🛒 VIEW CART
def Cart(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session["uid"])
    cart = tbl_cart.objects.filter(user=user, cart_status=0)

    # ✅ Update quantity only
    if request.method == "POST" and "update_cart" in request.POST:
        for item in cart:
            qty = request.POST.get(f"qty_{item.id}")
            if qty:
                item.cart_qnty = int(qty)
                item.save()

    # ✅ Recalculate total AFTER update
    total = 0
    for i in cart:
        price = int(i.product.product_price) if i.product and i.product.product_price else 0
        i.subtotal = price * int(i.cart_qnty)
        total += i.subtotal

    # ✅ Booking when Book Now clicked
    if request.method == "POST" and ("book_now" in request.POST or "confirm_booking" in request.POST or len(cart) > 0):
        # Only proceed to booking if clicked book_now or form submitted without update_cart
        if "update_cart" not in request.POST and total > 0:
            booking = tbl_booking.objects.create(
                user=user,
                booking_amount=total,
                booking_status=0
            )

            for item in cart:
                item.cart_status = 1
                item.booking = booking
                item.save()

            return redirect("User:Payment", booking.id)

    return render(request, "User/Cart.html", {
        "cart": cart,
        "total": total
    })


def AddToCart(request, id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session["uid"])
    product = tbl_product.objects.get(id=id)

    cart_item = tbl_cart.objects.filter(user=user, product=product, cart_status=0).first()

    if cart_item:
        cart_item.cart_qnty += 1
        cart_item.save()
    else:
        tbl_cart.objects.create(
            user=user,
            product=product,
            cart_qnty=1
        )

    return redirect("User:Cart")


def Booking(request, id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session['uid'])
    product = tbl_product.objects.filter(id=id).first()

    # If product exists, ensure it is in cart or prepare direct booking
    cart_items = tbl_cart.objects.filter(user=user, cart_status=0)

    total = 0
    for item in cart_items:
        price = int(item.product.product_price) if item.product and item.product.product_price else 0
        item.subtotal = price * int(item.cart_qnty)
        total += item.subtotal

    if request.method == "POST":
        if total > 0:
            booking = tbl_booking.objects.create(
                user=user,
                booking_amount=total,
                booking_status=0
            )
            for item in cart_items:
                item.cart_status = 1
                item.booking = booking
                item.save()
            return redirect('User:Payment', booking.id)
        elif product:
            booking = tbl_booking.objects.create(
                user=user,
                product=product,
                booking_amount=int(product.product_price),
                booking_status=0
            )
            return redirect('User:Payment', booking.id)

    return render(request, 'User/Booking.html', {
        'cart': cart_items,
        'total': total,
        'product': product
    })


def DeleteBooking(request, id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    try:
        cart_item = tbl_cart.objects.get(id=id, user_id=request.session['uid'])
        cart_item.delete()
    except tbl_cart.DoesNotExist:
        pass
    return redirect('User:Cart')


# 💳 PAYMENT
def Payment(request, id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    booking = tbl_booking.objects.get(id=id)

    if request.method == "POST":
        card = request.POST.get("txtacno") or ""
        name = request.POST.get("txtname") or ""

        tbl_payment.objects.create(
            payment_amount=booking.booking_amount,
            user=booking.user,
            booking=booking,
            card_no=card,
            card_name=name,
            payment_status=1
        )

        booking.booking_status = 1   # mark as paid / confirmed
        booking.save()

        return redirect("User:PaymentSuccess")

    return render(request, "User/Payment.html", {
        "booking": booking,
        "total": booking.booking_amount
    })


# ✅ SUCCESS
def PaymentSuccess(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')
    return render(request, "User/PaymentSuccess.html")


# 📦 MY ORDERS / MY BOOKINGS (ORDER HISTORY & TRACKING)
def MyBookings(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session['uid'])
    bookings = tbl_booking.objects.filter(user=user).order_by('-id')

    orders = []
    total_orders = bookings.count()
    active_orders = 0
    delivered_orders = 0

    for b in bookings:
        items = tbl_cart.objects.filter(booking=b)
        items_list = []
        if items.exists():
            for it in items:
                price = int(it.product.product_price) if it.product and it.product.product_price else 0
                qty = int(it.cart_qnty) if it.cart_qnty else 1
                items_list.append({
                    'item': it,
                    'product': it.product,
                    'price': price,
                    'qty': qty,
                    'subtotal': price * qty,
                })
        elif b.product:
            price = int(b.product.product_price) if b.product.product_price else b.booking_amount
            items_list.append({
                'item': None,
                'product': b.product,
                'price': price,
                'qty': 1,
                'subtotal': b.booking_amount,
            })

        status_code = b.booking_status
        if status_code in [0, 1, 2]:
            active_orders += 1
        elif status_code == 3:
            delivered_orders += 1

        # Status text, badge class and tracking step (1 to 4)
        if status_code == 0:
            status_text = "Pending Payment"
            status_badge = "badge-pending"
            step = 1
        elif status_code == 1:
            status_text = "Confirmed & Paid"
            status_badge = "badge-paid"
            step = 2
        elif status_code == 2:
            status_text = "Dispatched / Shipped"
            status_badge = "badge-shipped"
            step = 3
        elif status_code == 3:
            status_text = "Delivered"
            status_badge = "badge-delivered"
            step = 4
        elif status_code == 4:
            status_text = "Cancelled"
            status_badge = "badge-cancelled"
            step = 0
        else:
            status_text = "Order Placed"
            status_badge = "badge-pending"
            step = 1

        payment = tbl_payment.objects.filter(booking=b).first()

        orders.append({
            'booking': b,
            'items': items_list,
            'items_count': len(items_list),
            'status_code': status_code,
            'status_text': status_text,
            'status_badge': status_badge,
            'step': step,
            'is_cancelled': status_code == 4,
            'can_cancel': status_code in [0, 1],
            'payment': payment
        })

    return render(request, "User/MyBookings.html", {
        'orders': orders,
        'user': user,
        'total_orders': total_orders,
        'active_orders': active_orders,
        'delivered_orders': delivered_orders,
    })


# ❌ CANCEL BOOKING
def CancelBooking(request, id):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session['uid'])
    try:
        booking = tbl_booking.objects.get(id=id, user=user)
        if booking.booking_status in [0, 1]:
            booking.booking_status = 4  # Mark as cancelled
            booking.save()
    except tbl_booking.DoesNotExist:
        pass

    return redirect('User:MyBookings')


# ⚠ COMPLAINT
def Complaint(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session['uid'])

    if request.method == "POST":
        title = request.POST.get("title")
        details = request.POST.get("details")
        p_name = request.POST.get("Product")

        product_obj = tbl_product.objects.filter(product_name__icontains=p_name).first() if p_name else None

        tbl_complaint.objects.create(
            complaint_title=title,
            complaint_details=details,
            product=product_obj,
            user=user
        )
        return redirect("User:Complaint")

    complaints = tbl_complaint.objects.filter(user=user)
    return render(request, "User/Complaint.html", {
        "complaints": complaints
    })


# 💬 FEEDBACK
def Feedback(request):
    if request.method == "POST":
        tbl_feedback.objects.create(
            feedback_content=request.POST.get("content")
        )
        return redirect("User:Feedback")

    return render(request, "User/Feedback.html")


# ⭐ RATING
def Rating(request, pid):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    product = tbl_product.objects.get(id=pid)

    if request.method == "POST":
        tbl_rating.objects.create(
            rating_count=request.POST.get("rating"),
            rating_comment=request.POST.get("review"),
            product=product,
            user=tbl_user.objects.get(id=request.session['uid'])
        )
        return redirect("User:MyBookings")

    return render(request, "User/Rating.html", {"product": product})


def Products(request):
    products = tbl_product.objects.all()
    return render(request, "User/Products.html", {
        "products": products
    })


def Logout(request):
    request.session.flush()
    return redirect('Guest:Login')
