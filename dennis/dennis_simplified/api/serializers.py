from rest_framework import serializers
from base.models import Item

class ItemSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
