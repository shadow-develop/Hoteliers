from django.test import TestCase
from django.urls import reverse

from hoteliers.accounts.models import User
from django.contrib.auth import get_user_model

from hoteliers.web.models import Hotel

UserModel = get_user_model()

class HomePageViewTests(TestCase):
    VALID_HOTELIERS_USER_CREDENTIALS = {
        'email': 'test@test.com',
        'password': 'password'
    }

    VALID_USER_CREDENTIALS = {
        'first_name': 'test',
        'last_name': 'testov',
        'gender': 'male',
        'date_of_birth': '1997-08-26',
        'phone_number': '0886398383',
        'photo': None,
    }

    def __create_valid_HoteliersUser_and_User(self):
        hoteliers_user = UserModel.objects.create_user(**self.VALID_HOTELIERS_USER_CREDENTIALS)
        user = User.objects.create(
            **self.VALID_USER_CREDENTIALS,
            user=hoteliers_user
        )

        return hoteliers_user, user

    def test_when_there_are_no_hotels(self):
        hoteliers_user, user = self.__create_valid_HoteliersUser_and_User()

        self.client.force_login(hoteliers_user)

        hotels = list(Hotel.objects.filter(owner_id=user.user_id))
        self.client.get(reverse('user home', kwargs={'pk': user.pk}))

        self.assertEqual(len(hotels), 0)

    def test_when_there_are_hotels(self):
        hoteliers_user, user = self.__create_valid_HoteliersUser_and_User()
        Hotel.objects.create(
            name='TestHotel',
            stars=3,
            rooms=10,
            location='TestLocation',
            description='TestDescription',
            photo=None,
            owner=hoteliers_user,
        )

        self.client.force_login(hoteliers_user)

        hotels = list(Hotel.objects.filter(owner_id=user.user_id))
        self.client.get(reverse('user home', kwargs={'pk': user.pk}))

        self.assertEqual(len(hotels), 1)
