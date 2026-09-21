from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select
from main.models import Education, Experience
from django import forms

class EducationForm(ModelForm):
    secret_code = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Masukkan Kode Admin"
        }),
        label="Kode Rahasia Admin",
        required=True
    )

    class Meta:
        model = Education
        fields = ["institution", "degree", "field_of_study", "description", "start_year", "end_year"]
        labels = {
            "institution": "Nama Institusi",
            "degree": "Jenjang Pendidikan",
            "field_of_study": "Program Studi / Jurusan",
            "description": "Deskripsi",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai (Kosongkan jika masih berlangsung)",
        }
        widgets = {
            "institution": TextInput(attrs={"placeholder": "Universitas Indonesia"}),
            "degree": Select(),
            "field_of_study": TextInput(attrs={"placeholder": "Sistem Informasi"}),
            "description": Textarea(attrs={"placeholder": "Deskripsi kegiatan akademis...", "rows": 3}),
            "start_year": NumberInput(attrs={"placeholder": "2025"}),
            "end_year": NumberInput(attrs={"placeholder": "2029"}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail", "ended_at"]
        widgets = {
            'ended_at': forms.DateTimeInput(attrs={ 'type': 'datetime-local'}),
        }