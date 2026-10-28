# from django.shortcuts import render,redirect
# from Guest.models import *
# from Seller.models import *
# from User.models import *
# from .models import tbl_booking   
# from .models import tbl_cart
# from .models import tbl_product
# from .models import tbl_user
# def Homepage(request):
#     userdata = tbl_user.objects.get(id=request.session['uid'])
#     productdata = tbl_product.objects.all()
#     return render(request,'User/Homepage.html',{
#         'data': userdata,
#         'product': productdata
#     })
# def UserProfile(request):
#     userdata=tbl_user.objects.get(id= request.session['uid'])
#     return render(request,'User/UserProfile.html',{'data':userdata})

# def UserEditProfile(request):
#     userdata = tbl_user.objects.get(id=request.session['uid'])
#     district_data = tbl_district.objects.all()
#     if request.method == "POST":
#         userdata.user_name = request.POST.get('name')
#         userdata.user_email = request.POST.get('email')
#         userdata.user_contact = request.POST.get('contact')
#         userdata.user_address = request.POST.get('address')
#         place_id = request.POST.get('place')
#         userdata.place = tbl_place.objects.get(id=place_id)
#         userdata.save()
#         return redirect('User:UserProfile')
#     else:
#         place_data = tbl_place.objects.filter(district_id=userdata.place.district_id)
#         return render(request,'User/UserEditProfile.html',{
#                 'data': userdata,
#                 'district': district_data,
#                 'place': place_data
#             })

# def UserChangePassword(request):
#     user = tbl_user.objects.get(id=request.session['uid'])
#     if request.method == "POST":
#         old_pass = request.POST.get("txt_old")
#         new_pass = request.POST.get("txt_new")
#         re_pass = request.POST.get("txt_re")
#         if user.user_password == old_pass:
#             if new_pass == re_pass:
#                 user.user_password = new_pass
#                 user.save()
#                 return render(request,"User/UserChangePassword.html",{
#                         "msg":"Password Changed Successfully"
#                 })
#             else:
#                 return render(request,"User/UserChangePassword.html",{
#                         "msg":"New Passwords do not match"
#                 })
#         else:
#             return render(request,"User/User/UserChangePassword.html",{
#                     "msg":"Old Password Incorrect"
#             })
#     else:
#         return render(request,"User/UserChangePassword.html")




# # 🛒 VIEW CART
# def Cart(request):
#     user = tbl_user.objects.get(id=request.session["uid"])
#     cart = tbl_cart.objects.filter(user=user, cart_status=0)

#     total = 0
#     for i in cart:
#         i.subtotal = int(i.product.product_price) * int(i.cart_qnty)
#         total += i.subtotal

#     if request.method == "POST":
#         booking = tbl_booking.objects.create(
#             user=user,
#             booking_amount=total
#         )

#         for item in cart:
#             item.cart_status = 1
#             item.booking = booking
#             item.save()

#         return redirect("User:Payment", booking.id)

#     return render(request, "User/Cart.html", {
#         "cart": cart,
#         "total": total
#     })

# # 📦 BOOKING
# def Booking(request):
#     user = tbl_user.objects.get(id=request.session['uid'])
#     cart_items = tbl_cart.objects.filter(user=user)

#     total = 0
#     for item in cart_items:
#         total += int(item.product.product_price) * int(item.cart_qnty)
#         booking = tbl_booking.objects.create(user=user,booking_amount=total)
#     # Clear cart
#         cart_items.delete()

#     return redirect('User:Cart')

# # 💳 PAYMENT
# def Payment(request, id):
#     booking = tbl_booking.objects.get(id=id)

#     if request.method == "POST":
#         card = request.POST.get("card")
#         name = request.POST.get("name")

#         tbl_payment.objects.create(
#             payment_amount=booking.booking_amount,
#             user=booking.user,
#             booking=booking,
#             card_no=card,
#             card_name=name
#         )

#         booking.booking_status = 1
#         booking.save()

#         return redirect("User:Success")

#     return render(request, "User/Payment.html", {"booking": booking})


# # ✅ SUCCESS
# def PaymentSuccess(request):
#     return render(request, "User/PaymentSuccess.html")


# # ⭐ RATING
# def Rating(request, pid):
#     product = tbl_product.objects.get(id=pid)

#     if request.method == "POST":
#         tbl_rating.objects.create(
#             rating_count=request.POST.get("rating"),
#             rating_comment=request.POST.get("review"),
#             product=product,
#             user=tbl_user.objects.get(id=request.session['uid'])
#         )
#         return redirect("User:Cart")

#     return render(request, "User/Rating.html", {"product": product})


# # ⚠ COMPLAINT
# def Complaint(request):
#     user = tbl_user.objects.get(id=request.session['uid'])
#     complaints = tbl_complaint.objects.filter(user=user)

#     if request.method == "POST":
#         tbl_complaint.objects.create(
#             complaint_title=request.POST.get("title"),
#             complaint_details=request.POST.get("details"),
#             user=user
#         )
#         return redirect("User:Complaint")

#     return render(request, "User/Complaint.html", {"complaints": complaints})


# # 💬 FEEDBACK
# def Feedback(request):
#     if request.method == "POST":
#         tbl_feedback.objects.create(
#             feedback_content=request.POST.get("content")
#         )
#         return redirect("User:Feedback")

#     return render(request, "User/Feedback.html")

# def ViewProducts(request):
#     products = tbl_product.objects.all()

#     return render(request, "User/ViewProducts.html", {
#         "products": products
#     })

# def AddToCart(request, id):
#     user = tbl_user.objects.get(id=request.session["uid"])
#     product = tbl_product.objects.get(id=id)

#     # check if already in cart
#     cart_item = tbl_cart.objects.filter(user=user, product=product, cart_status=0).first()

#     if cart_item:
#         cart_item.cart_qnty += 1
#         cart_item.save()
#     else:
#         tbl_cart.objects.create(
#             user=user,
#             product=product,
#             cart_qnty=1
#         )

#     return redirect("User:Cart")   # 🔥 IMPORTANT


from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *
from .models import tbl_booking   
from .models import tbl_cart
from .models import tbl_product
from .models import tbl_user
from django.shortcuts import get_object_or_404

def Homepage(request):
    userdata = tbl_user.objects.get(id=request.session['uid'])
    productdata = tbl_product.objects.all()
    return render(request,'User/Homepage.html',{
        'data': userdata,
        'product': productdata
    })
def UserProfile(request):
    userdata=tbl_user.objects.get(id= request.session['uid'])
    return render(request,'User/UserProfile.html',{'data':userdata})

def UserEditProfile(request):
    userdata = tbl_user.objects.get(id=request.session['uid'])
    district_data = tbl_district.objects.all()
    if request.method == "POST":
        userdata.user_name = request.POST.get('name')
        userdata.user_email = request.POST.get('email')
        userdata.user_contact = request.POST.get('contact')
        userdata.user_address = request.POST.get('address')
        place_id = request.POST.get('place')
        userdata.place = tbl_place.objects.get(id=place_id)
        userdata.save()
        return redirect('User:UserProfile')
    else:
        place_data = tbl_place.objects.filter(district_id=userdata.place.district_id)
        return render(request,'User/UserEditProfile.html',{
                'data': userdata,
                'district': district_data,
                'place': place_data
            })

def UserChangePassword(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        old_pass = request.POST.get("txt_old")
        new_pass = request.POST.get("txt_new")
        re_pass = request.POST.get("txt_re")
        if user.user_password == old_pass:
            if new_pass == re_pass:
                user.user_password = new_pass
                user.save()
                return render(request,"User/UserChangePassword.html",{
                        "msg":"Password Changed Successfully"
                })
            else:
                return render(request,"User/UserChangePassword.html",{
                        "msg":"New Passwords do not match"
                })
        else:
            return render(request,"User/User/UserChangePassword.html",{
                    "msg":"Old Password Incorrect"
            })
    else:
        return render(request,"User/UserChangePassword.html")




# 🛒 VIEW CART
def Cart(request):
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
        i.subtotal = int(i.product.product_price) * int(i.cart_qnty)
        total += i.subtotal

    # ✅ Booking only when Book Now clicked
    if request.method == "POST" and "book_now" in request.POST:
        booking = tbl_booking.objects.create(
            user=user,
            booking_amount=total
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
    
def Booking(request, id):
    cart_items = tbl_cart.objects.filter(user=request.session['uid'])

    total = 0
    for item in cart_items:
        price = int(item.product.product_price)
        qty = int(item.cart_qnty)
        item.subtotal = price * qty
        total += item.subtotal

    if request.method == "POST":
        booking = tbl_booking.objects.create(
            user_id=request.session['uid'],
            booking_amount=total
        )

        # OPTIONAL: create booking items table (recommended design)

        return redirect('User:Payment', booking.id)

    return render(request, 'User/Booking.html', {
        'cart': cart_items,
        'total': total
    })
def DeleteBooking(request, id):
    cart_item = tbl_cart.objects.get(id=id)
    cart_item.delete()
    return redirect('User:Booking', id=id)

# 💳 PAYMENT
def Payment(request, id):
    booking = tbl_booking.objects.get(id=id)

    if request.method == "POST":
        booking.booking_status = 1   # mark as paid
        booking.save()

        return redirect("User:PaymentSuccess")  # or booking page

    return render(request, "User/Payment.html", {
        "booking": booking
    })

# ✅ SUCCESS
def PaymentSuccess(request):
    return render(request, "User/PaymentSuccess.html")


# ⭐ RATING
def Rating(request, pid):
    product = tbl_product.objects.get(id=pid)

    if request.method == "POST":
        tbl_rating.objects.create(
            rating_count=request.POST.get("rating"),
            rating_comment=request.POST.get("review"),
            product=product,
            user=tbl_user.objects.get(id=request.session['uid'])
        )
        return redirect("User:Cart")

    return render(request, "User/Rating.html", {"product": product})


# ⚠ COMPLAINT
def Complaint(request):
    if 'uid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=request.session['uid'])
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

def Products(request):
    products = tbl_product.objects.all()

    return render(request, "User/Products.html", {
        "products": products
    })

def AddToCart(request, id):
    user = tbl_user.objects.get(id=request.session["uid"])
    product = tbl_product.objects.get(id=id)

    # check if already in cart
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

    return redirect("User:Cart")   # 🔥 IMPORTANT


def Logout(request):
    request.session.flush()   
    return redirect('Guest:Login')  

