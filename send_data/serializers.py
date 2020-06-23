from rest_framework import serializers
from .models import data_store

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data_store
        fields = '__all__'
