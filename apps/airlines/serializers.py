from django.conf import settings

from rest_framework import serializers

from .utils import AirplaneUtils


class AirplaneSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    passengers = serializers.IntegerField()
    tank_capacity = serializers.SerializerMethodField()
    per_passenger_consumption = serializers.SerializerMethodField()
    per_minute_fuel_consumption = serializers.SerializerMethodField()
    max_fly_minutes = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'passengers', 'tank_capacity', 'fuel_consumption')

    def get_tank_capacity(self, obj):
        return AirplaneUtils(obj).tank_capacity

    def get_per_passenger_consumption(self, obj):
        return AirplaneUtils(obj).per_passenger_consumption

    def get_per_minute_fuel_consumption(self, obj):
        return AirplaneUtils(obj).per_minute_fuel_consumption

    def get_max_fly_minutes(self, obj):
        return AirplaneUtils(obj).max_fly_minutes


class AirlineSerializer(serializers.Serializer):
    airplanes = AirplaneSerializer(many=True)

    class Meta:
        fields = ('airplanes',)

    def validate_airplanes(self, value):
        if len(value) > settings.MAX_PLANES:
            raise serializers.ValidationError(
                'Max %s planes allowed.' % settings.MAX_PLANES)
        return value
