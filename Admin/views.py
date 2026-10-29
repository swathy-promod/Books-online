from django.shortcuts import render, redirect
from .models import *
from Guest.models import tbl_user, tbl_seller


def Homepage(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    user_count = tbl_user.objects.count()
    seller_count = tbl_seller.objects.count()
    pending_seller_count = tbl_seller.objects.filter(seller_status=0).count()

    return render(request, "Admin/Homepage.html", {
        "user_count": user_count,
        "seller_count": seller_count,
        "pending_seller_count": pending_seller_count
    })


# Create your views here.
def AdminRegistration(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    if request.method == 'POST':
        name = request.POST.get('txtname')
        email = request.POST.get('txtEmail')
        password = request.POST.get('txtpass')

        tbl_admin.objects.create(
            admin_name=name,
            admin_email=email,
            admin_password=password,
        )
        return redirect("Admin:AdminRegistration")

    else:
        admin_data = tbl_admin.objects.all()
        return render(request, 'Admin/AdminRegistration.html', {'admins': admin_data})


def AdminDelete(request, did):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_admin.objects.get(id=did).delete()
    return redirect("Admin:AdminRegistration")


def AdminEdit(request, eid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    edit_Admin = tbl_admin.objects.get(id=eid)
    admin_data = tbl_admin.objects.all()

    if request.method == 'POST':
        name = request.POST.get('txtname')
        email = request.POST.get('txtEmail')
        password = request.POST.get('txtpass')

        edit_Admin.admin_name = name
        edit_Admin.admin_email = email
        edit_Admin.admin_password = password
        edit_Admin.save()

        return redirect("Admin:AdminRegistration")

    else:
        return render(request, 'Admin/AdminRegistration.html', {
            'data': admin_data,      # for table loop
            'edit': edit_Admin       # for edit form
        })


def Category(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    if request.method == 'POST':
        name = request.POST.get('txtname')
        tbl_category.objects.create(
            category_name=name,
        )
        return redirect("Admin:Category")
    else:
        category_data = tbl_category.objects.all()
        return render(request, 'Admin/Category.html', {'categ': category_data})


def CategoryDelete(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:Category")


def CategoryEdit(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    edit_category = tbl_category.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get("txtname")
        edit_category.category_name = name
        edit_category.save()
        return redirect("Admin:Category")
    else:
        return render(request, 'Admin/Category.html', {'data': edit_category})


def District(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    if request.method == "POST":
        name = request.POST.get("txtdist")
        tbl_district.objects.create(
            district_name=name,
        )
        return redirect("Admin:District")
    else:
        district_data = tbl_district.objects.all()
        return render(request, 'Admin/District.html', {'dist': district_data})


def DistrictDelete(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:District")


def DistrictEdit(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    edit_district = tbl_district.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get("txtdist")
        edit_district.district_name = name
        edit_district.save()
        return redirect("Admin:District")
    else:
        return render(request, 'Admin/District.html', {'data': edit_district})


def Place(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    if request.method == "POST":
        name = request.POST.get("txtplace")
        district_id = request.POST.get("dis")
        district_obj = tbl_district.objects.get(id=district_id)
        tbl_place.objects.create(
            place_name=name,
            district_id=district_obj
        )
        return redirect("Admin:Place")
    else:
        district_Data = tbl_district.objects.all()
        place_data = tbl_place.objects.all()
        return render(request, 'Admin/Place.html', {'pla': place_data, 'disData': district_Data})


def PlaceDelete(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:Place")


def PlaceEdit(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    edit_place = tbl_place.objects.get(id=id)
    district_Data = tbl_district.objects.all()
    place_data = tbl_place.objects.all()
    if request.method == 'POST':
        name = request.POST.get("txtplace")
        district_id = request.POST.get("dis")
        district_obj = tbl_district.objects.get(id=district_id)
        edit_place.place_name = name
        edit_place.district_id = district_obj  # Fixed: was edit_place.district
        edit_place.save()
        return redirect("Admin:Place")
    else:
        return render(request, 'Admin/Place.html', {
            'data': edit_place,
            'disData': district_Data,
            'pla': place_data
        })


def Genre(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    genre_data = tbl_genre.objects.all()
    category_data = tbl_category.objects.all()

    if request.method == "POST":
        gname = request.POST.get("txtgenrename")
        cat_id = request.POST.get("sel_category")

        category = None
        if cat_id:
            category = tbl_category.objects.get(id=cat_id)

        tbl_genre.objects.create(
            genre_name=gname,
            category_id=category
        )

        return redirect("Admin:Genre")

    return render(request, 'Admin/Genre.html', {
        'genre': genre_data,
        'category': category_data
    })


def GenreDelete(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    tbl_genre.objects.get(id=id).delete()
    return redirect("Admin:Genre")


def GenreEdit(request, id):
    if 'aid' not in request.session:
        return redirect('Guest:Login')
    edit_genre = tbl_genre.objects.get(id=id)
    category_data = tbl_category.objects.all()

    if request.method == "POST":
        edit_genre.genre_name = request.POST.get("txtgenrename")

        cat_id = request.POST.get("sel_category")
        if cat_id:
            edit_genre.category_id = tbl_category.objects.get(id=cat_id)

        edit_genre.save()
        return redirect("Admin:Genre")

    return render(request, 'Admin/Genre.html', {
        'editdata': edit_genre,
        'category': category_data
    })


# 🏢 SELLER APPROVAL WORKFLOW
def SellerList(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    pending_sellers = tbl_seller.objects.filter(seller_status=0).order_by('-id')
    accepted_sellers = tbl_seller.objects.filter(seller_status=1).order_by('-id')
    rejected_sellers = tbl_seller.objects.filter(seller_status=2).order_by('-id')

    return render(request, 'Admin/SellerList.html', {
        'pending': pending_sellers,
        'accepted': accepted_sellers,
        'rejected': rejected_sellers,
        'pending_count': pending_sellers.count(),
        'accepted_count': accepted_sellers.count(),
        'rejected_count': rejected_sellers.count(),
        'total_count': tbl_seller.objects.count()
    })


def accSeller(request, sid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    seller = tbl_seller.objects.get(id=sid)
    seller.seller_status = 1  # Accepted / Approved
    seller.save()
    return redirect('Admin:SellerList')


def rejSeller(request, sid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    seller = tbl_seller.objects.get(id=sid)
    seller.seller_status = 2  # Rejected
    seller.save()
    return redirect('Admin:SellerList')


# 👥 USER MANAGEMENT WORKFLOW
def UserList(request):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    users = tbl_user.objects.all().order_by('-id')
    active_users = tbl_user.objects.filter(user_status=0).count()
    blocked_users = tbl_user.objects.filter(user_status=2).count()

    return render(request, 'Admin/UserList.html', {
        'users': users,
        'total_count': users.count(),
        'active_count': active_users,
        'blocked_count': blocked_users
    })


def accUser(request, uid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=uid)
    user.user_status = 0  # Active / Unblocked
    user.save()
    return redirect('Admin:UserList')


def rejUser(request, uid):
    if 'aid' not in request.session:
        return redirect('Guest:Login')

    user = tbl_user.objects.get(id=uid)
    user.user_status = 2  # Blocked / Inactive
    user.save()
    return redirect('Admin:UserList')
