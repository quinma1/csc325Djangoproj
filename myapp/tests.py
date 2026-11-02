from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_displays_welcome_message(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Welcome to the Home Page!')


class AboutViewTests(TestCase):
    def test_about_displays_welcome_message(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'Welcome to the About Page!')


class InfoApiTests(TestCase):
    def test_info_returns_course(self):
        data = self.client.get(reverse('info')).json()
        self.assertEqual(data['course'], 'CSC325')

    def test_info_returns_project(self):
        data = self.client.get(reverse('info')).json()
        self.assertEqual(data['project'], 'Django CI/CD')

    def test_info_returns_student(self):
        data = self.client.get(reverse('info')).json()
        self.assertEqual(data['student'], 'Matt')

    def test_info_returns_semester(self):
        data = self.client.get(reverse('info')).json()
        self.assertEqual(data['semester'], 'Fall 2026')