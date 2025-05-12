# serializers.py
from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'name', 'skills', 'experience','projects','certifications']
        # Optionally set the default value for "certifications" here too, if needed
        extra_kwargs = {
            'projects': {'required': False},     # Make certifications optional in the API
        }
        extra_kwargs = {
            'certifications': {'required': False},     # Make certifications optional in the API
        }
       
    
      
