from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class UserModelChoiceField(forms.models.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label=_('Username'))
    first_name = forms.CharField(label=_('Name'))
    last_name = forms.CharField(label=_('Surname'))
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label=_('Confirm the password'),
        widget=forms.PasswordInput(),
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if self.instance:
            if User.objects.exclude(id=self.instance.pk).filter(username__iexact=username).first():  # noqa: E501
                return super().clean_username()
            return username
        return super().clean_username()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
    )
