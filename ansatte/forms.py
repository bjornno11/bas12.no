from django import forms
from django.contrib.auth.models import User
from .models import Ansatt

class AnsattUserForm(forms.ModelForm):
    # Felter fra User
    username = forms.CharField(max_length=150, label="Brukernavn")
    email = forms.EmailField(required=True, label="E-post")
    password = forms.CharField(widget=forms.PasswordInput, label="Passord")

    class Meta:
        model = Ansatt
        fields = [
            "username", "email", "password",   # User-felter
            "roller", "aktiv",
            "adresse", "telefon",
            "personnummer", "ansatt_dato", "kjonn",
        ]

    def save(self, commit=True):
        # Opprett User først
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        user = User.objects.create_user(username=username, email=email, password=password)

        ansatt = super().save(commit=False)
        ansatt.user = user
        if commit:
            ansatt.save()
            self.save_m2m()
        return ansatt
