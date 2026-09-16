from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Education
from main.forms import EducationForm


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
    json_response = get_education_json(request)
    education_objects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )
    education_list = [item.object for item in education_objects]
    search_query = request.GET.get("search", "").strip()

    context = {
        "name": "Ilman Ghani Awliya",
        "education_list": education_list,
        "search_query": search_query,
    }
    return render(request, "education.html", context)


def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Ilman Ghani Awliya",
        "form": form,
    }
    return render(request, "education_form.html", context)


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")