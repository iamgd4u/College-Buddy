from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from auth import forms


# Create your views here.
class Login(LoginView):
    template_name = "auth/login.html"
    
class Logout(LogoutView):
    pass

class Signup(View):
    def get(self, request):
        context = {
            "form": forms.SignupForm()
        }
        return render(request, "auth/signup.html", context)

    def post(self, request):
        form = forms.SignupForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request,user)
            return redirect('/')
        else:
            context = {
                "form" : form
            }
            return render(request, "auth/signup.html", context)

