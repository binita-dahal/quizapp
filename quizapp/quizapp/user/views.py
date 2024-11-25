from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User


# Create your views here.
def loginUser(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            if user is not None:
                return redirect('/quiz')
            else:
                return render(request, 'login.html')
        return render(request, 'login.html')
    else:
        return redirect('/quiz')
        
    
 
def register(request):
    if request.user.is_anonymous:
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            email = request.POST['email']

        # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                error_message = 'Username is already taken. Please choose a different username.'
                return render(request, 'register.html', {'error_message': error_message})

            # Create a new user
            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                        last_name=last_name, email=email)
            # You can perform additional actions here, such as sending a confirmation email
        
         # Redirect to a success page or login page
            return redirect('login')
        else:
            return render(request, 'register.html')
    else:
        return redirect('/')

def logoutUser(request):
    logout(request)
    return redirect('/')