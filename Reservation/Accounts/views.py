# Accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import UserFarmerRegistrationForm, UserDriverRegistrationForm
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group 
from django.contrib.auth.decorators import login_required
from Driver.models import Vehicle


@login_required
def custom_logout(request):
    logout(request)
    return redirect('home')  



def home_accounts(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'home.html', {'vehicles': vehicles, 'driver_id': request.user.id})

def useregister(request):
     return render(request,'chooserole.html') 


def register_farmer(request):
    if request.method == 'POST':
        form = UserFarmerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Add the user to the 'driver' group
            farmer_group = Group.objects.get(name='farmer')
            user.groups.add(farmer_group)
            user.is_customer = True
            user.save()

            return redirect('login')
    else:
        form = UserFarmerRegistrationForm()

    return render(request, 'Farmer/registerfarmer.html', {'form': form})

def register_driver(request):
    if request.method == 'POST':
        form = UserDriverRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            driver_group = Group.objects.get(name='driver')
            user.groups.add(driver_group)

            user.is_staff = True
            user.save()

            return redirect('login')
    else:
        form = UserDriverRegistrationForm()

    return render(request, 'Driver/registerdriver.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                # Additional logging for debugging
                print(f"User {username} logged in with groups: {[group.name for group in user.groups.all()]}")

                # Check all group names
                print(f"All group names: {[group.name for group in Group.objects.all()]}")

                # Check the user's role and redirect accordingly
                if 'farmer' in [group.name for group in user.groups.all()]:
                    return redirect('home_farmer')
                elif 'driver' in [group.name for group in user.groups.all()]:
                    return redirect('home_driver')
                else:
                    return redirect('home')  # Default redirect if not in any group

            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'Accounts/registration/login.html', {'form': form})




from django.http import HttpResponse

def view_driver_profile(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='driver').exists():
            # ตรวจสอบว่าผู้ใช้เป็นเจ้าของรถหรือไม่
            is_vehicle_owner = False
            if hasattr(request.user, 'vehicles'):
                is_vehicle_owner = True

            context = {
                'user': request.user,
                'is_vehicle_owner': is_vehicle_owner,
            }
            return render(request, 'Driver/driver_profile.html', context)
        else:
            return render(request, 'Driver/driver_profile.html')  # หรือหน้าโปรไฟล์ของคนขับรถ
    else:
        # หากไม่ได้เข้าสู่ระบบ ให้แสดงหน้าโปรไฟล์ได้ทันที
        return render(request, 'Driver/driver_profile.html')

@login_required
def profile_update(request):
    form = None
    if 'farmer' in [group.name for group in request.user.groups.all()]:
        if request.method == 'POST':
            form = UserFarmerUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_update')
        else:
            form = UserFarmerUpdateForm(instance=request.user)
        return render(request, 'profile_farmer.html', {'form': form})  # ปรับเปลี่ยนเพื่อใช้ profile_farmer.html
    elif 'driver' in [group.name for group in request.user.groups.all()]:
        if request.method == 'POST':
            form = UserDriverUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile_update')
        else:
            form = UserDriverUpdateForm(instance=request.user)
        return render(request, 'profile_driver.html', {'form': form})  # ปรับเปลี่ยนเพื่อใช้ profile_driver.html
