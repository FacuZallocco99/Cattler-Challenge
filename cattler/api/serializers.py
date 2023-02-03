from rest_framework import serializers
from .models import Animal, Troop, Corral, Lot


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = "__all__"


class TroopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Troop
        fields = "__all__"


class CorralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corral
        fields = "__all__"


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = "__all__"
