from rest_framework import serializers
from .models import PrivateItem

class PrivateItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateItem
        fields = '__all__'
