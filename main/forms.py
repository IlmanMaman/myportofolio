from django.forms import ModelForm, TextInput, Textarea, NumberInput, Select
from main.models import Education

class EducationForm(ModelForm):
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