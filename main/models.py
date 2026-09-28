import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

    starred_by = models.ManyToManyField(User, related_name="starred_experiences", blank=True)

class Education(models.Model):
    DEGREE_CHOICES = [
        ('high_school', 'High School'),
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate'), # Perbaikan typo 'postgradiate' menjadi 'postgraduate'
        ('certification', 'Certification / Course'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='undergraduate')
    field_of_study = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

    starred_by = models.ManyToManyField(User, related_name='starred_educations', blank=True)

    def __str__(self):
        return f"{self.get_degree_display()} at {self.institution}"

    @property
    def is_ongoing(self):
        return self.end_year is None

    def total_stars(self):
        return self.starred_by.count()