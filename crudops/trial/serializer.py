from django.db.models import fields
from rest_framework import serializers
from .models import Trial

class TrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trial
        fields = '__all__'