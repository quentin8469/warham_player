from django import forms
from account.models import CustomUser


class NewUserForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': "Nom d'utilisateur"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Confirmez votre mot de passe"}))

    class Meta:
        """
        """
        model = CustomUser
        fields = ("username", "password1", "password2")