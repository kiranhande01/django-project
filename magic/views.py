from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import District, Tahsil, Village, Project
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout



def map_view(request):
    districts = District.objects.all()
    projects = Project.objects.all().select_related('village__tahsil__district')
    return render(request, 'map.html', {'districts': districts, 'projects': projects})

def get_tahsils(request, district_id):
    tahsils = Tahsil.objects.filter(district_id=district_id).values('id', 'name', 'boundary')
    return JsonResponse(list(tahsils), safe=False)

def get_villages(request, tahsil_id):
    villages = Village.objects.filter(tahsil_id=tahsil_id).values('id', 'name', 'boundary')
    return JsonResponse(list(villages), safe=False)

def get_project(request, village_id):
    project = Project.objects.filter(village_id=village_id).select_related('village__tahsil__district').first()
    if project:
        return JsonResponse({
            'name': project.name,
            'latitude': project.latitude,
            'longitude': project.longitude,
            'polygon_data': project.polygon_data,
            'village': project.village.name,
            'tahsil': project.village.tahsil.name,
            'district': project.village.tahsil.district.name,
        })
    return JsonResponse({}, status=404)

def get_project_by_id(request, project_id):
    project = Project.objects.select_related('village__tahsil__district').filter(id=project_id).first()
    if project:
        return JsonResponse({
            'name': project.name,
            'latitude': project.latitude,
            'longitude': project.longitude,
            'polygon_data': project.polygon_data,
            'village': project.village.name,
            'tahsil': project.village.tahsil.name,
            'district': project.village.tahsil.district.name,
        })
    return JsonResponse({}, status=404)







def base(request):
    return render(request,'base.html')



def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("map_view")  # Redirect to the dashboard or home page
        else:
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")


def register(request):
    context={}
    if request.method=='POST':
        un=request.POST['uname']
        em=request.POST['uemail']
        p=request.POST['upass']
        cp=request.POST['ucpass']
        print(un,em,p,cp)
        if un=='' or em=='' or p=='' or cp=='':
            context['error_msg']='ALL FIELDS ARE REQUIRED'
            return render(request,'register.html',context)
       
        elif len(p)<8:
            context['error_msg']='PASSWORD MUST BE  GREATER THAN OR EQUAL TO 8'
            return render(request,'register.html',context)

        elif p!=cp:
            context['error_msg']='PASSWORD AND CONFIRM PASSWORD NOT MATCHED'
            return render(request,'register.html',context)

        else:
            u = User.objects.create(username=em, email=em)  # Use email as username

            u.set_password(p)
            u.save()

            return redirect('/login')
        



        
    else:
        return render(request,'register.html')



from django.contrib.auth import logout as auth_logout

def logout_view(request):
    auth_logout(request)
    return redirect('/login')
