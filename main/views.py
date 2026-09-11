from django.shortcuts import render
from main.models import Experience, Education

def show_main(request):
    context = {
        "name": "Ilman Ghani Awliya",  
        "npm": "2506656803",            
        "study_program": "S1 Sistem Informasi", 
        "bio": "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik pada UI/UX Design dan Web Development.",
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Ilman Ghani Awliya", 
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all()
    context = {
        'education_list': education_list,
    }
    return render(request, 'education.html', context)