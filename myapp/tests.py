from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_displays_welcome_message(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, "Welcome to the Home Page!")


class AboutViewTests(TestCase):
    def test_about_displays_welcome_message(self):
        response = self.client.get(reverse("about"))

        self.assertContains(response, "Welcome to the About Page!")
