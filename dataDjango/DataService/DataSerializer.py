from rest_framework import serializers
from .models import ModelPP


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelPP
        fields = '__all__'

    def create(self, validated_data):
        return ModelPP.objects.create(**validated_data)