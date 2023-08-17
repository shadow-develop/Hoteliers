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

        hotel.owner = self.user
        if commit:
            hotel.save()

        return hotel

    class Meta:
        model = Hotel
        fields = ('name', 'stars', 'rooms', 'location', 'description', 'photo',)
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows': 5,
                }
            ),
        }


class HotelEditForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Hotel
        fields = '__all__'
        exclude = ['owner']


class HotelDeleteForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Hotel
        fields = ()


class HotelGalleryPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, hotel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hotel = hotel
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        hotel = super().save(commit=False)

        hotel.owner = self.user
        if commit:
            hotel.save()

        return hotel
