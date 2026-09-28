import os
import datetime
from dotenv import load_dotenv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm

load_dotenv()
SECRET_KEY = os.getenv("PORTFOLIO_SECRET_KEY")


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


def get_education_json(request):
    search_query = request.GET.get("search", "").strip()
    education_list = Education.objects.all()
    if search_query:
        education_list = education_list.filter(institution__icontains=search_query)
    
    education_json = serializers.serialize("json", education_list)
    return HttpResponse(education_json, content_type="application/json")


def show_education(request):
    search_query = request.GET.get("search", "").strip()
    education_list = Education.objects.all()
    
    if search_query:
        education_list = education_list.filter(institution__icontains=search_query)

    context = {
        "name": "Ilman Ghani Awliya",
        "education_list": education_list,
        "search_query": search_query,
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = EducationForm(request.POST or None)
    if request.method == "POST":
        input_secret = request.headers.get("X-Secret-Code") or request.POST.get("secret_code")
        
        if input_secret != SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Anda tidak memiliki akses untuk menambah data.")
            return render(request, "education_form.html", {"name": "Ilman Ghani Awliya", "form": form})

        if form.is_valid():
            form.save()
            messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
            return redirect("main:show_education")

    context = {
        "name": "Ilman Ghani Awliya",
        "form": form,
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        input_secret = request.headers.get("X-Secret-Code") or request.POST.get("secret_code")
        
        if input_secret != SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Data gagal dihapus.")
            return redirect("main:show_education")

        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def show_experience(request):
    context = {
        "name": "Ilman Ghani Awliya",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def get_experience_json(request):
    experience_list = Experience.objects.all()
    experience_json = serializers.serialize(
        "json", experience_list, use_natural_foreign_keys=True
    )
    return HttpResponse(experience_json, content_type="application/json")

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
            raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST":
        input_secret = request.headers.get("X-Secret-Code") or request.POST.get("secret_code")
        
        if input_secret != SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Anda tidak memiliki akses untuk menambah data.")
            return render(request, "experience_form.html", {"name": "Ilman Ghani Awliya", "form": form, "title": "Tambah Experience"})

        if form.is_valid():
            form.save()
            messages.success(request, "Pengalaman berhasil ditambahkan!")
            return redirect("main:show_experience")

    context = {
        "name": "Ilman Ghani Awliya",
        "form": form,
        "title": "Tambah Experience",
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST":
        input_secret = request.headers.get("X-Secret-Code") or request.POST.get("secret_code")
        
        if input_secret != SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Anda tidak memiliki akses untuk mengubah data.")
            return render(request, "experience_form.html", {"name": "Ilman Ghani Awliya", "form": form, "title": "Edit Experience"})

        if form.is_valid():
            form.save()
            messages.success(request, "Pengalaman berhasil diperbarui!")
            return redirect("main:show_experience")

    context = {
        "name": "Ilman Ghani Awliya",
        "form": form,
        "title": "Edit Experience",
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        input_secret = request.headers.get("X-Secret-Code") or request.POST.get("secret_code")
        
        if input_secret != SECRET_KEY:
            messages.error(request, "Kode rahasia salah! Data gagal dihapus.")
            return redirect("main:show_experience")

        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Ilman Ghani Awliya",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        # Set cookie last_login
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Ilman Ghani Awliya",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Ilman Ghani Awliya",
        # ... context lainnya ...
        "last_login": last_login,
    }
    return render(request, "index.html", context)

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
    return redirect("main:show_experience")