# resume_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse 

def project_home(request):
    return JsonResponse({'message': 'Welcome to the Resume Backend API! Visit /api/resumes/'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', project_home),     # include your app's urls here
]
