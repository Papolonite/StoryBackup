from django.db.models import fields
from django.forms import ModelForm
from .models import MataKuliah

# Form Class
class MataKuliahForm(ModelForm):
    class Meta:
        model = MataKuliah
        fields = ['nama','sks','dosen','kelas','semester','deskripsi']
