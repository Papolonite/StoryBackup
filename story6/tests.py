from django.test import TestCase , Client
from django.urls import resolve
from . import models
from .models import People, Activities
from .views import register, display, register_activites
import datetime

# Create your tests here.
class Story6Test(TestCase):
    # Setting up the database
    def setUp(self):
        self.activites = Activities.objects.create(name="Raid Kamoshida Palace",date=datetime.date(2020,5,6))
        People.objects.create(full_name="Ren Amamiya", nickname="Joker", gender="Male", birthday=datetime.date(2000,5,13), activities_registered = self.activites)
        People.objects.create(full_name="Makoto Nijima", nickname="Queen", gender="Female", birthday=datetime.date(1998,4,23), activities_registered = self.activites)

    # Checking Database
    def test_check_amount_people_database(self):
        self.assertEqual(len(People.objects.all()), 2)

    def test_check_amount_acitivites_database(self):
        self.assertEqual(len(Activities.objects.all()), 1)

    # Checking URLS
    def test_register_url_exist(self):
        response = Client().get('/story-6/register/')
        self.assertEqual(response.status_code,200)

    def test_display_url_exist(self):
        response = Client().get('/story-6/')
        self.assertEqual(response.status_code,200)

    def test_register_activities_url_exist(self):
        response = Client().get('/story-6/register-activities/')
        self.assertEqual(response.status_code,200)

    # Checking Views
    def test_register_views_exist(self):
        found = resolve('/story-6/register/')
        self.assertEqual(found.func, register)

    def test_display_views_exist(self):
        found = resolve('/story-6/')
        self.assertEqual(found.func, display)

    def test_register_views_exist(self):
        found = resolve('/story-6/register-activities/')
        self.assertEqual(found.func, register_activites)

    # Checking Templates
    def test_register_templates_exist(self):
        response = Client().get('/story-6/register/')
        self.assertTemplateUsed(response, 'register_people.html')

    def test_display_templates_exist(self):
        response = Client().get('/story-6/')
        self.assertTemplateUsed(response, 'display_activities.html')

    def test_register_activities_templates_exist(self):
        response = Client().get('/story-6/register-activities/')
        self.assertTemplateUsed(response, 'register_activities.html')

    # Checking if HTML displaying models
    def test_if_HTML_display_models(self):
        response = Client().get('/story-6/')
        html_response = response.content.decode('utf8')
        self.assertIn("Raid Kamoshida Palace", html_response)
        self.assertIn("Ren Amamiya", html_response)
    
    # Checking Form Exist & works
    def test_saving_a_POST_activities_request(self):
        response = Client().post('/story-6/register-activities/', data={'name': 'Lunch', 'date': '2020-12-12'})
        amount = models.Activities.objects.filter(name="Lunch").count()
        self.assertEqual(amount, 1)

    def test_saving_a_POST_request(self):
        activites2 = Activities.objects.get(pk=1).pk
        response = Client().post('/story-6/register/', data={'full_name': 'Ann Takamaki', 'nickname': 'Panther', 'gender' : 'Female', 'birthday' : '2001-04-07', 'activities_registered' : activites2})
        amount = models.People.objects.filter(full_name='Ann Takamaki').count()
        self.assertEqual(amount, 1)