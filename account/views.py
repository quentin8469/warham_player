from re import template
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, DetailView
from account.forms import NewUserForm
from django.contrib.auth.views import LogoutView, LoginView

from account.models import CustomUser
# Create your views here.

class SignUpView(CreateView):
    form_class = NewUserForm
    template_name = "signup/signup.html"
    success_url = '/login/'


class LogoutView(LogoutView):
    next_page = '/login/'

    
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

class UserProfilDetail(DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = "profil/profil_details.html"
    
    def get_context_data(self, **kwargs):
        context = {}
        user = CustomUser.object.get(id=self.kwargs['pk'])
        context['user'] = user
        
        return super().get_context_data(**context) # get the default context data
