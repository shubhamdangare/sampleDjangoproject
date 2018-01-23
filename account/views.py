from django.shortcuts import render, HttpResponse, redirect ,reverse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from account.forms import Registrationform
from django.contrib.auth.decorators import login_required


# Create your views here.
from account.models import Userprofile


def home(request):
    name = 'shubham'
    number = [1, 2, 3, 4, 5]
    args = {
        'name': name,
        'number': number
    }
    return render(request, 'account/home.html', args)


def register(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:home'))

    else:
        form = Registrationform
        args = {'forms': form}
        return render(request, 'account/register.html', args)


@login_required
def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user

    args = {'user':user}
    return render(request, 'account/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:profile'))

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/editprofile.html', args)


def changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('account:home'))

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'account/changepass.html', args)
