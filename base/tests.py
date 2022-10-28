from django.test import TestCase
from django.contrib.auth.models import User
from base.models import UserProfile as Profile
from django.contrib.gis.geos import Point

# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self):
        self.admin = User.objects.create(username="admin", is_superuser=True, is_staff=True, is_active=True)
        self.staff = User.objects.create(username="staff",  is_superuser=False, is_staff=True, is_active=True)
        self.user = User.objects.create(username="user",  is_superuser=False, is_staff=False, is_active=True)

    def test_users_can_have_a_profile(self):
        """Animals that can speak are correctly identified"""
        Profile.objects.create(user=self.admin, home_address="344 England St., Johannesburg",
            phone_number="27105004139", location=Point(30.9641, -29.8474))
        Profile.objects.create(user=self.staff, home_address="565 Mandela Av., Cape City", 
            phone_number="+27105004539", location=Point(28.0488, -26.1951))
        Profile.objects.create(user=self.user, home_address="1231 John Smith St., Durban", 
            phone_number="27105005148", location=Point(28.1150, -26.1887))
        self.assertEqual(self.admin.profile.home_address, '344 England St., Johannesburg')
        self.assertEqual(Profile.objects.all().count(), 3)
    
