from django.shortcuts import render,redirect
from .models import *
from Admin.models import  *
from .models import tbl_seller, tbl_place


def Homepage(request):
    return render(request,"Guest/Homepage.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('txtemail')
        password = request.POST.get('txtpass')

        admin = tbl_admin.objects.filter(admin_email=email, admin_password=password).first()
        user = tbl_user.objects.filter(user_email=email, user_password=password).first()
        seller = tbl_seller.objects.filter(seller_email=email, seller_password=password).first()

        if admin:
            request.session['aid'] = admin.id
            return redirect("Admin:Homepage")

        elif user:
            request.session['uid'] = user.id
            return redirect("User:Homepage")

        elif seller:
            if seller.seller_status == 0:
                return render(request, "Guest/Login.html", {"msg": "Pending approval"})
            elif seller.seller_status == 1:
                request.session['sid'] = seller.id
                return redirect("Seller:Homepage")
            elif seller.seller_status == 2:
                return render(request, "Guest/Login.html", {"msg": "Rejected"})
        
        return render(request, 'Guest/Login.html', {"msg": "Invalid email or password"})

    return render(request, 'Guest/Login.html')

def UserRegistration(request):
    if request.method == 'POST':
        name = request.POST.get('txtname')
        email = request.POST.get('txtEmail')
        password = request.POST.get('txtpass')
        contact = request.POST.get('txtcontact')
        gender = request.POST.get('gender')
        photo = request.FILES.get('txtfile')
        bio = request.POST.get('txtbio')   
        district_id = request.POST.get("dis")
        place_id = request.POST.get("pla")
        district_obj = tbl_district.objects.get(id=district_id)
        place_obj = tbl_place.objects.get(id=place_id)
        tbl_user.objects.create(
            user_name=name,
            user_email=email,
            user_password=password,
            user_contact=contact,
            user_gender=gender,
            place=place_obj,
            user_photo=photo,
            user_bio=bio
        )
        return redirect("Guest:UserRegistration")
    else:
        userdata = tbl_user.objects.all()
        disData = tbl_district.objects.all()
        pladata = tbl_place.objects.all()
        return render(request,'Guest/UserRegistration.html', {
            'user': userdata,
            'pla': pladata,
            'disData': disData
        })
   
def SellerRegistration(request):
    disData = tbl_district.objects.all()
    pla = tbl_place.objects.all()

    if request.method == "POST":
        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        password = request.POST.get("txt_password")
        address = request.POST.get("txt_address")
        photo = request.FILES.get("txt_photo")
        proof = request.FILES.get("txt_proof")

        place_id = request.POST.get("pla")   # ✅ FIXED (was sel_place)
        doj = request.POST.get("txt_doj")
        doe = request.POST.get("txt_doe")
        licence = request.POST.get("txt_licence")

        place = tbl_place.objects.get(id=place_id)

        tbl_seller.objects.create(
            seller_name=name,
            seller_email=email,
            seller_contact=contact,
            seller_password=password,
            seller_address=address,
            seller_photo=photo,
            seller_proof=proof,
            place=place,
            seller_doj=doj,
            seller_doe=doe,
            seller_licence=licence
        )

        return redirect("Guest:SellerRegistration")

    return render(request, "Guest/SellerRegistration.html", {
        "disData": disData,
        "pla": pla
    })

def ajaxplace(request):
    did = request.GET.get('did')
    placedata = tbl_place.objects.filter(district_id=did)
    return render(request, 'Guest/AjaxPlace.html', {'plc': placedata})


def Logout(request):
    request.session.flush()   
    return redirect('Guest:Login')   
    
def index(request):
    return render(request,'Guest/index.html')