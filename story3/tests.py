from django.test import TestCase, Client
from django.urls import resolve
from . import models
from .models import Semester, MataKuliah
from .views import profile, home, createMatkul, viewMatkul,viewMatkulDetail, deleteView

# Create your tests here.
class Story3Test(TestCase):
    def setUp(self):
        self.semester = Semester.objects.create(term_choices="Ganjil", year="2019/2020")
        MataKuliah.objects.create(nama="PPW", sks= 3, dosen="Ara", kelas="D", semester= self.semester, deskripsi="Hello")

    # Checking Database
    def test_check_amount_semester_database(self):
        self.assertEqual(len(Semester.objects.all()), 1)

    def test_check_amount_matakuliah_database(self):
        self.assertEqual(len(MataKuliah.objects.all()), 1)

    # Checking URLS
    def test_story3_url_exist(self):
        response = Client().get('/story-3/')
        self.assertEqual(response.status_code,200)

    def test_home_url_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code,200)

    def test_create_url_exist(self):
        response = Client().get('/create-matkul/')
        self.assertEqual(response.status_code,200)

    def test_view_url_exist(self):
        response = Client().get('/view-matkul/')
        self.assertEqual(response.status_code,200)

    def test_view_detail_url_exist(self):
        response = Client().get('/view-matkul/1')
        self.assertEqual(response.status_code,200)

    # Checking templates
    def test_story3_templates_exist(self):
        response = Client().get('/story-3/')
        self.assertTemplateUsed(response, 'my_profile.html')

    def test_home_templates_exist(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'home.html')

    def test_create_templates_exist(self):
        response = Client().get('/create-matkul/')
        self.assertTemplateUsed(response, 'create_matkul.html')

    def test_view_templates_exist(self):
        response = Client().get('/view-matkul/')
        self.assertTemplateUsed(response, 'view_matkul.html')

    def test_view_detail_templates_exist(self):
        response = Client().get('/view-matkul/1')
        self.assertTemplateUsed(response, 'view_matkul_detail.html')

    # Checking delete views
    def test_view_detail_delete_url_exist(self):
        response = Client().get('/view-matkul/1/delete')
        self.assertEqual(len(MataKuliah.objects.all()), 0)

    # Checking if Templates/HTML Displaying models
    def test_if_Story5_HTML_display_models(self):
        MataKuliah.objects.create(nama="PPW", sks= 3, dosen="Ara", kelas="D", semester= self.semester, deskripsi="Hello")
        response = Client().get('/view-matkul/')
        html_response = response.content.decode('utf8')
        self.assertIn('PPW', html_response)

    # Checking form exist & works
    def test_saving_a_POST_activities_request(self):
        semester = Semester.objects.get(pk=1).pk
        response = Client().post('/create-matkul/', data={'nama': 'SDA','sks': 4, 'dosen': 'Bu Mei', 'kelas':'C', 'semester' : semester, 'deskripsi' : 'Test'})
        amount = models.MataKuliah.objects.filter(nama="SDA").count()
        self.assertEqual(amount, 1)

