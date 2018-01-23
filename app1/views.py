from django.shortcuts import redirect


def redirect_login(request):
    return redirect('/account/login')
