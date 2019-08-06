from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm,UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.decorators import login_required
from events.models import Events

def index(request):
    AllEvents = Events.objects.all()
    counter = 0
    trendy_list = []


    if len(AllEvents) != 0:
        for the_event in AllEvents :
            if the_event.current_attendants < the_event.expected_attendants:
                if len(trendy_list) < 3:
                    trendy_list.append(the_event)

        return render(request, 'main/index.html', {'trendy_list':trendy_list})
    else:
        return render(request, 'main/index.html')
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        # profile_form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            # profile.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'Your account has been created! You are now able to log in now!!!')
            print("save!!! user")
            return redirect('/login')
    else:
        form = NewUserForm()
        # profile_form = ProfileForm()
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:index")

# def login_request(request):
#     form = AuthenticationForm()
#     return render(request = request,
#                   template_name = "main/login.html",
#                   context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('main:index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
@login_required
def edit_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print("Save img")
            messages.success(request, f'Your account has been updated!')
            return redirect('/account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'main/edit.html', {
        'u_form': u_form,
        'p_form': p_form
    })
@login_required
def showAcc_info(request):
    # acc_show = User.objects.get(id=acc_id)
    # return render(req,'acc.html',{"acc_show":acc_show})
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('/account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'main/acc.html', {
        'u_form': u_form,
        'p_form': p_form
    })
