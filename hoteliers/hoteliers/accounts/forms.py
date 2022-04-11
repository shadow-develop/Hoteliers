from django.contrib.auth import forms as auth_forms, get_user_model

from hoteliers.common.helpers import BootstrapFormMixin
from django import forms

from hoteliers.accounts.models import User


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     profile = User(
    #         # first_name=self.cleaned_data['first_name'],
    #         # last_name=self.cleaned_data['last_name'],
    #         # gender=self.cleaned_data['gender'],
    #         # date_of_birth=self.cleaned_data['date_of_birth'],
    #         # photo=self.cleaned_data['picture'],
    #         # user=user,
    #     )
    #
    #     if commit:
    #         profile.save()
    #     return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1',)


class LoginProfileForm(BootstrapFormMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)
