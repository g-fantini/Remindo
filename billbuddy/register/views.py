# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        p_reg_form = ProfileRegisterForm(request.POST)

        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = ProfileRegisterForm(request.POST, instance=user.profile)
            p_reg_form.full_clean()
            p_reg_form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        p_reg_form = ProfileRegisterForm()
    context = {
        'user_form': form,
        'profile_form': p_reg_form
    }
    return render(request, "register/register.html", context)
    