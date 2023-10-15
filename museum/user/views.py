from django.shortcuts import render, HttpResponseRedirect
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from catalog.models import Basket
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('catalog:home'))
        else:
            print("form is not valid")
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались.')
            return HttpResponseRedirect(reverse('user:login'))
        else:
            print("form is not valid")
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'user/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('catalog:home'))

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            print('Form is not valid', form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {
        'title': 'Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'user/profile.html', context)