from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from hoteliers.accounts.models import User
from hoteliers.web.models import Hotel

UserModel = get_user_model()


class UserDetailsViewTests(TestCase):
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

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('user details', kwargs={
            'pk': 1,
        }))
        self.assertTemplateUsed('accounts/user_details.html')

        self.assertEqual(404, response.status_code)

    def test_when_all_valid__expect_correct_template(self):
        hoteliers_user, user = self.__create_valid_HoteliersUser_and_User()
        self.client.force_login(hoteliers_user)

        response = self.client.get(reverse('user details', kwargs={'pk': user.pk}))
        self.assertTemplateUsed(response, 'accounts/user_details.html')

    def test_when_user_has_1_hotel1__expect_number_of_hotels_to_equal_1(self):
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
        self.client.get(reverse('user details', kwargs={'pk': user.pk}))

        self.assertEqual(len(hotels), 1)

    def test_when_no_hotels__expect_0(self):
        hoteliers_user, user = self.__create_valid_HoteliersUser_and_User()

        self.client.force_login(hoteliers_user)

        hotels = list(Hotel.objects.filter(owner_id=user.user_id))
        self.client.get(reverse('user details', kwargs={'pk': user.pk}))

        self.assertEqual(len(hotels), 0)
