from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='def', password = 'himanshu')
        self.userb = User.objects.create_user(username='abc', password = 'himanshu')

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_following(self):
        first = self.user
        second = self.userb
        first.profile.followers.add(second) #we added a follower here
        qs = second.following.filter(user = first) #checking that second user is following first
        self.assertTrue(qs.exists())
        first_user_following_no_one = first.following.all()
        self.assertFalse(first_user_following_no_one.exists())