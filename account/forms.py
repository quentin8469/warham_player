from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser


class NewUserForm(UserCreationForm):

    class Meta:
        """
        """
        model = CustomUser
        fields = ("username", "email", )