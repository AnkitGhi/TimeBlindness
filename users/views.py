from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'task/profile.html')
          # Replace 'profile' with your profile URL name
    
    return render(request, 'task/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        
    return render(request,'users/signup.html',{'form': form})

@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)