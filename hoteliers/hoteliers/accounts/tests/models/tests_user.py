from django.core.exceptions import ValidationError
from django.test import TestCase
from hoteliers.accounts.models import User
from hoteliers.web.models import UserModel


class UserTests(TestCase):
    VALID_HOTELIERS_USER_CREDENTIALS = {
        'email': 'test@test.com',
        'password': 'password'
    }

    VALID_USER_CREDENTIALS = {
        'first_name': 'Ivan',
        'last_name': 'Pazvantov',
        'gender': 'Male',
        'date_of_birth': '1997-08-26',
        'phone_number': '0886398383',
        'photo': None,
    }

    def __create_valid_hoteliersUser(self):
        hoteliers_user = UserModel.objects.create_user(**self.VALID_HOTELIERS_USER_CREDENTIALS)

        return hoteliers_user

    def __create_valid_HoteliersUser_and_User(self):
        hoteliers_user = UserModel.objects.create_user(**self.VALID_HOTELIERS_USER_CREDENTIALS)
        user = User.objects.create(
            **self.VALID_USER_CREDENTIALS,
            user=hoteliers_user
        )

        return hoteliers_user, user

    def test_profile_create__when_first_name_contains_letters_only__expect_to_success(self):
        _, user = self.__create_valid_HoteliersUser_and_User()
        user.save()

    def test_profile_create__when_first_name_contains_a_hashtag__expect_to_fail(self):
        first_name = '#Ivan'
        hoteliers_user = self.__create_valid_hoteliersUser()
        user = User(
            first_name=first_name,
            last_name=self.VALID_USER_CREDENTIALS['last_name'],
            gender=self.VALID_USER_CREDENTIALS['gender'],
            date_of_birth=self.VALID_USER_CREDENTIALS['date_of_birth'],
            phone_number=self.VALID_USER_CREDENTIALS['phone_number'],
            photo=self.VALID_USER_CREDENTIALS['photo'],
            user_id=hoteliers_user.pk
        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_number__expect_to_fail(self):
        first_name = 'Ivan1'
        hoteliers_user = self.__create_valid_hoteliersUser()
        user = User(
            first_name=first_name,
            last_name=self.VALID_USER_CREDENTIALS['last_name'],
            gender=self.VALID_USER_CREDENTIALS['gender'],
            date_of_birth=self.VALID_USER_CREDENTIALS['date_of_birth'],
            phone_number=self.VALID_USER_CREDENTIALS['phone_number'],
            photo=self.VALID_USER_CREDENTIALS['photo'],
            user_id=hoteliers_user.pk
        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Iv an'
        hoteliers_user = self.__create_valid_hoteliersUser()
        user = User(
            first_name=first_name,
            last_name=self.VALID_USER_CREDENTIALS['last_name'],
            gender=self.VALID_USER_CREDENTIALS['gender'],
            date_of_birth=self.VALID_USER_CREDENTIALS['date_of_birth'],
            phone_number=self.VALID_USER_CREDENTIALS['phone_number'],
            photo=self.VALID_USER_CREDENTIALS['photo'],
            user_id=hoteliers_user.pk
        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_to_success(self):
        user = User(**self.VALID_USER_CREDENTIALS)
        expected_full_name = f'{self.VALID_USER_CREDENTIALS["first_name"]} {self.VALID_USER_CREDENTIALS["last_name"]}'
        self.assertEqual(expected_full_name, user.__str__())
