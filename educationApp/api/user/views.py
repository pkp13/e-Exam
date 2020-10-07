from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# Create your views here.

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def signup(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile_form.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()




    return render(request, 'signup.html', {
        'user_form': user_form,
        'profile_form':profile_form,
        'registered':registered
    })


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            # else:
            #     return HttpResponse("<h1>Account not active</h1>")
        
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request, 'signin.html', {})