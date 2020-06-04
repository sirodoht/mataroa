from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as DjUserCreationForm
from django.core.mail import mail_admins


class UserCreationForm(DjUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username"]


class InterestForm(forms.Form):
    email = forms.EmailField()

    def send_email(self):
        body = "There is a person interested in Mataroa premium!"
        body += f"\nThis is their email: {self.cleaned_data.get('email')}"
        body += "\n"
        body += "\nBest,"
        body += "\nPython"

        mail_admins("Interest form response", body)
