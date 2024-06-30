from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse("Invalid login. Please try again.")
    return render(request, 'auth/login.html')

def custom_logout(request):
    logout(request)
    return redirect('/logout_success/')

def logout_success(request):
    return render(request, 'auth/success.html')

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html', {'user': request.user})