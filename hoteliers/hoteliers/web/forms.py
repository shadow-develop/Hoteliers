from django import forms
from hoteliers.common.helpers import BootstrapFormMixin
from hoteliers.web.models import Hotel


class HotelCreateForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        hotel = super().save(commit=False)

        hotel.user = self.user
        if commit:
            hotel.save()

        return hotel

    class Meta:
        model = Hotel
        fields = ('name', 'stars', 'location', 'photo', 'description', 'owner')
