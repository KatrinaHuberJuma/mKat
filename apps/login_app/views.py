
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User


def root(request):
    print("*** login app > views > root ***"*4)
    print(User.objects.all())
    return render(request, "login_app/index.html")

def login(request):
    errors = {}
    if request.method == "POST":
        possible_user = User.objects.filter(email=request.POST["email"])
        try:
            this_user = possible_user[0]
            if request.POST["password"] == this_user.hashed_pw:
                request.session['first_name'] = this_user.first_name
                request.session['last_name'] = this_user.last_name
                request.session['id'] = this_user.id
                return redirect("/")
            errors['password_oopsie_error']= "You seem to have forgotten your password. Too bad for you, we for sure don't save your plaintext password so get a new email and come back."
        except:
            errors['email_oopsie_error']=  "No user exists with this email, go ahead and register!"
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
    return redirect("/login")

def reg(request):
    if request.method == "POST":
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = User.objects.basic_validator(request.POST) 
        if request.POST["password"] != request.POST["confirm_password"]:
            errors['pw_confrimation_fail'] = "Password does not match confirmation password"     
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/login')
        else:
            password = request.POST["confirm_password"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, hashed_pw=password)
            request.session['first_name'] = new_user.first_name
            request.session['last_name'] = new_user.last_name
    return redirect("/")

def success(request):
    if "first_name" in request.session: # there is also a decorator to do this, see make_charts.views.index
        return render(request, "login_app/success.html") 
    return redirect('/login')

def logout(request):
    request.session.clear()
    return redirect('/login')