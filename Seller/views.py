# from django.shortcuts import render, redirect
# from .models import *
# from Admin.models import *
# from Guest.models import *

# def Homepage(request):
#     sellerdata=tbl_seller.objects.get(id= request.session['sid'])
#     return render(request,'Seller/Homepage.html',{'data':sellerdata})
# def SellerProfile(request):
#     sid = request.session.get("sid")

#     if not sid:
#         return redirect("Guest:Login")   

#     seller = tbl_seller.objects.get(id=sid)

#     return render(request, "Seller/SellerProfile.html", {
#         "seller": seller
#     })

# def SellerEditProfile(request):
#     sid = request.session.get("sid")

#     if not sid:
#         return redirect("Guest:Login")

#     seller = tbl_seller.objects.get(id=sid)

#     if request.method == "POST":
#         seller.seller_name = request.POST.get("name")
#         seller.seller_email = request.POST.get("email")
#         seller.seller_contact = request.POST.get("contact")
#         seller.seller_address = request.POST.get("address")
#         seller.save()

#         return redirect("Seller:SellerProfile")

#     return render(request, "Seller/SellerEditProfile.html", {
#         "seller": seller
#     })
   
# def SellerChangePassword(request):
#     seller = tbl_seller.objects.get(id=request.session['sid'])
#     if request.method == "POST":
#         old_pass = request.POST.get("txt_old")
#         new_pass = request.POST.get("txt_new")
#         re_pass = request.POST.get("txt_re")
#         if seller.seller_password == old_pass:
#             if new_pass == re_pass:
#                 seller.seller_password = new_pass
#                 seller.save()
#                 return render(request,"Seller/SellerChangePassword.html",{
#                         "msg": "Password Changed Successfully"
#                 })
#             else:
#                 return render(request,"Seller/SellerChangePassword.html",{
#                         "msg": "New Passwords do not match"
#                 })
#         else:
#             return render(request,"Seller/SellerChangePassword.html",{
#                     "msg": "Old Password Incorrect"
#             })
#     else:
#         return render(request, "Seller/SellerChangePassword.html")


# # ================= TYPE =================
# def Type(request):
#     data = tbl_type.objects.all()

#     if request.method == "POST":
#         name = request.POST.get("txt_name")
#         tbl_type.objects.create(type_name=name)
#         return redirect("Seller:Type")

#     return render(request, "Seller/Type.html", {"data": data})


# def DeleteType(request, id):
#     tbl_type.objects.get(id=id).delete()
#     return redirect("Seller:Type")


# # ================= PRODUCT =================
# def Product(request):
#     product = tbl_product.objects.all()
#     types = tbl_type.objects.all()

#     if request.method == "POST":
#         name = request.POST.get("txtname")
#         desc = request.POST.get("txtdesc")
#         price = request.POST.get("txtprice")
#         photo = request.FILES.get("txtphoto")
#         type_id = request.POST.get("type")

#         type_obj = None
#         if type_id:
#             type_obj = tbl_type.objects.get(id=type_id)

#         tbl_product.objects.create(
#             product_name=name,
#             product_description=desc,
#             product_price=price,
#             product_photo=photo,
#             type_id=type_obj,
#             seller_id=tbl_seller.objects.get(id=request.session["sid"])
#         )

#         return redirect("Seller:Product")

#     return render(request, "Seller/Product.html", {
#         "productData": product,
#         "typeData": types
#     })

# def DeleteProduct(request, id):
#     tbl_product.objects.get(id=id).delete()
#     return redirect("Seller:Product")


# # ================= PRODUCT DETAILS =================
# def ProductDetails(request):
#     data = tbl_productdetails.objects.all()
#     products = tbl_product.objects.all()

#     if request.method == "POST":
#         author = request.POST.get("txt_author")
#         content = request.POST.get("txt_content")
#         written = request.POST.get("txt_written")
#         published = request.POST.get("txt_published")
#         pid = request.POST.get("sel_product")

#         tbl_productdetails.objects.create(
#             productdetails_author_name=author,
#             productdetails_content=content,
#             productdetails_written=written,
#             productdetails_published=published,
#             product_id=tbl_product.objects.get(id=pid)
#         )
#         return redirect("Seller:ProductDetails")

#     return render(request, "Seller/ProductDetails.html", {
#         "data": data,
#         "products": products
#     })


# def DeleteProductDetails(request, id):
#     tbl_productdetails.objects.get(id=id).delete()
#     return redirect("Seller:ProductDetails")


# # ================= STOCK =================
# def Stock(request):
#     data = tbl_stock.objects.all()
#     products = tbl_product.objects.all()

#     if request.method == "POST":
#         qty = request.POST.get("txt_qty")
#         pid = request.POST.get("sel_product")

#         tbl_stock.objects.create(
#             stock_qnty=qty,
#             product_id=tbl_product.objects.get(id=pid)
#         )
#         return redirect("Seller:Stock")

#     return render(request, "Seller/Stock.html", {
#         "data": data,
#         "products": products
#     })


# def DeleteStock(request, id):
#     tbl_stock.objects.get(id=id).delete()
#     return redirect("Seller:Stock")

from django.shortcuts import render, redirect
from .models import tbl_product, tbl_type
from .models import tbl_seller
from User.models import *
from Seller.models import *


def Homepage(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')

    sellerdata = tbl_seller.objects.get(id=request.session['sid'])

    return render(request, "Seller/Homepage.html", {
        'seller': sellerdata
    })


def SellerProfile(request):
    sellerdata=tbl_seller.objects.get(id= request.session['sid'])
    return render(request,'Seller/SellerProfile.html', {'data':sellerdata})

def SellerEditProfile(request):
    sellerdata = tbl_seller.objects.get(id=request.session['sid'])
    district_data = tbl_district.objects.all()
    if request.method == "POST":
        sellerdata.user_name = request.POST.get('name')
        sellerdata.user_email = request.POST.get('Email')
        sellerdata.user_contact = request.POST.get('contact')
        sellerdata.user_address = request.POST.get('address')
        place_id = request.POST.get('place')
        sellerdata.place = tbl_place.objects.get(id=place_id)
        sellerdata.save()
        return redirect('Seller:SellerProfile')
    else:
        place_data = tbl_place.objects.filter(district=sellerdata.place.district)
        return render(request,'Seller/SellerEditProfile.html',{
                'data': sellerdata,
                'district': district_data,
                'place': place_data
            })
   
def SellerChangePassword(request):
    seller = tbl_seller.objects.get(id=request.session['sid'])
    if request.method == "POST":
        old_pass = request.POST.get("txt_old")
        new_pass = request.POST.get("txt_new")
        re_pass = request.POST.get("txt_re")
        if seller.seller_password == old_pass:
            if new_pass == re_pass:
                seller.seller_password = new_pass
                seller.save()
                return render(request,"Seller/SellerChangePassword.html",{
                        "msg": "Password Changed Successfully"
                })
            else:
                return render(request,"Seller/SellerChangePassword.html",{
                        "msg": "New Passwords do not match"
                })
        else:
            return render(request,"Seller/SellerChangePassword.html",{
                    "msg": "Old Password Incorrect"
            })
    else:
        return render(request, "Seller/SellerChangePassword.html")

def AddProduct(request):
    types = tbl_type.objects.all()
    products = tbl_product.objects.all()

    if request.method == "POST":
        tbl_product.objects.create(
            product_name=request.POST.get("txtname"),
            product_description=request.POST.get("txtdesc"),
            product_price=request.POST.get("txtprice"),
            product_photo=request.FILES.get("txtphoto"),
            type_id=tbl_type.objects.get(id=request.POST.get("type")),
            seller_id=tbl_seller.objects.get(id=request.session['sid'])
        )

    return render(request, "Seller/Product.html", {
        "types": types,
        "productData": products
    })


def ProductDelete(request,id):
    tbl_product.objects.get(id=id).delete()
    return redirect("Seller:AddProduct")


def ViewBooking(request):
    cartdata = tbl_cart.objects.all()
    productdata=tbl_product.objects.all()
    bookingdata=tbl_booking.objects.all()
    return render(request,"Seller/ViewBooking.html",{
        'cartdata': cartdata,
        'productdata':productdata,
        'bookingdata':bookingdata 
        })


def ViewComplaint(request):
    seller = request.session['sid']

    complaints = tbl_complaint.objects.filter(
        product__seller_id=seller
    )

    return render(request, "Seller/ViewComplaint.html", {
        "complaints": complaints
    })
    
def Reply(request, rid):
    rep = tbl_complaint.objects.get(id=rid)

    if request.method == "POST":
        reply = request.POST.get('reply')   # ✅ match textarea name

        rep.complaint_reply = reply
        rep.complaint_status = 1
        rep.save()

        return redirect('Seller:ViewComplaint')

    return render(request, 'Seller/Reply.html', {
        'complaint': rep   # ✅ send object
    })

def AddStock(request,pid):
    stock = tbl_stock.objects.filter(product=pid)

    if request.method == 'POST':
        stock_qnty = request.POST.get('txtstock')
        product = tbl_product.objects.get(id=pid)

        tbl_stock.objects.create(
            stock_qnty=stock_qnty,
            product=product
        )
        return redirect("Seller:AddStock", pid=pid)

    return render(request,'Seller/AddStock.html',{
        'sto':stock,
        'pid':pid
    })

def StockDelete(request, id, pid):
    tbl_stock.objects.get(id=id).delete()
    return redirect("Seller:AddStock", pid=pid)
def StockEdit(request,id,pid):
    editstock = tbl_stock.objects.get(id=id)
    stock = tbl_stock.objects.filter(product=pid)

    if request.method=='POST':
        editstock.stock_qnty = request.POST.get("txtstock")
        editstock.save()
        return redirect("Seller:AddStock", pid=pid)

    return render(request,'Seller/AddStock.html',{
        'pid':pid,
        'data':editstock,
        'sto':stock
    })



def Logout(request):
    request.session.flush()   
    return redirect('Guest:Login')  

