from django.test import TestCase
from profiles.views import profile

class TestProfilesViews(TestCase):

    def test_get_profiles_page(self):
        page = self.client.get("/profiles/")
        self.assertTemplateUsed('profile.html')

    def update_profiles_page(self):
        page = self.client.get("profiles/")
        self.assertTemplateUsed('profile_update.html')

