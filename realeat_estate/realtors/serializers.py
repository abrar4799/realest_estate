from rest_framework import serializers
from .models import Realtor

class RealtorsSerializer(serializers.ModelSerializer):
    model = Realtor
    fields= '__all__'