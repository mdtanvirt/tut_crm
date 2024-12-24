from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check the logged in user
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            # then we have to redirect to a page
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')

    else:
        return render(request, 'home.html', {})

# this function we will use if we want to use any seperate login page
#def login_view(request):
#    pass

def logout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')
