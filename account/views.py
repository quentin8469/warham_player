from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from account.forms import NewUserForm
from django.contrib.auth.views import LogoutView, LoginView
# Create your views here.

class SignUpView(CreateView):
    form_class = NewUserForm
    template_name = "signup/signup.html"
    success_url = '/accounts/'


class LogoutView(LogoutView):
    next_page = '/accounts/'

    
class LoginView(LoginView):
    template_name = "registration/login.html"
    success_url = '/liste_personnages/'
    
    
def connexion(request):
    """
    :param request:
    :return:
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/liste_personnages/')

    return render(request, "registration/login.html")



