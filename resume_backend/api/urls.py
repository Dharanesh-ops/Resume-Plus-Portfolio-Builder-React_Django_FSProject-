# api/urls.py
from django.urls import path
from .views import ResumeListCreateView, ResumeDetailView

urlpatterns = [
    path('resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),  # For listing and creating resumes
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),  # For retrieving, updating, and deleting specific resumes
]
