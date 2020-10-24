from django.db import models

# Create your models here.
class Semester(models.Model):
    term_choices = [
        ('Ganjil','Ganjil'),
        ('Genap','Genap')
    ]
    term_choices = models.CharField(max_length=6, choices=term_choices, default= 'Ganjil')
    year = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.year} {self.term_choices}'

class MataKuliah(models.Model):
    nama = models.CharField(max_length=100)
    sks = models.PositiveSmallIntegerField()
    dosen = models.CharField(max_length=100)
    kelas = models.CharField(max_length=50)
    semester = models.ForeignKey("Semester", on_delete=models.CASCADE)
    deskripsi = models.TextField()

    def __str__(self):
        return f'{self.nama}'
