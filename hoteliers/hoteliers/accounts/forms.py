from django.contrib.auth import forms as auth_forms, get_user_model

from hoteliers.common.helpers import BootstrapFormMixin
from django import forms

from hoteliers.accounts.models import User


class CreateUserForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=User.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=User.LAST_NAME_MAX_LENGTH,
    )
    gender = forms.ChoiceField(
        choices=User.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = User(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class LoginUserForm(BootstrapFormMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'gender', 'email', 'password',)


class EditUserForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['date_of_birth'].required = False
        self.fields['phone_number'].required = False
        self.fields['photo'].required = False

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'photo')
