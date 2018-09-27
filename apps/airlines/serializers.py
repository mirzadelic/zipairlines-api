from django.conf import settings

from rest_framework import serializers

from .utils import AirplaneUtils


class AirplaneSerializer(serializers.Serializer):
    '''
    Serializer for single airplane, which return read only calculated data:
     - tank_capacity
     - per_passenger_consumption
     - per_minute_fuel_consumption
     - max_fly_minutes
     - fuel_required
    '''

    id = serializers.IntegerField()
    passengers = serializers.IntegerField()
    tank_capacity = serializers.SerializerMethodField()
    per_passenger_consumption = serializers.SerializerMethodField()
    per_minute_fuel_consumption = serializers.SerializerMethodField()
    max_fly_minutes = serializers.SerializerMethodField()
    fuel_required = serializers.SerializerMethodField()

    class Meta:
        fields = ('id', 'passengers', 'tank_capacity', 'fuel_consumption')

    def validate(self, data):
        airplane = AirplaneUtils(data)
        if airplane.fuel_required > airplane.tank_capacity:
            raise serializers.ValidationError(
                'Plane cannot accept that much passengers.')
        return data

    def get_tank_capacity(self, obj):
        return AirplaneUtils(obj).tank_capacity

    def get_per_passenger_consumption(self, obj):
        return AirplaneUtils(obj).per_passenger_consumption

    def get_per_minute_fuel_consumption(self, obj):
        return AirplaneUtils(obj).per_minute_fuel_consumption

    def get_max_fly_minutes(self, obj):
        return AirplaneUtils(obj).max_fly_minutes

    def get_fuel_required(self, obj):
        return AirplaneUtils(obj).fuel_required


class AirlineSerializer(serializers.Serializer):
    '''
    Serializer for all airplanes, with validation for max allowed planes.
    '''

    airplanes = AirplaneSerializer(many=True)

    class Meta:
        fields = ('airplanes',)

    def validate_airplanes(self, value):
        if len(value) > settings.MAX_PLANES:
            raise serializers.ValidationError(
                'Max %s planes allowed.' % settings.MAX_PLANES)
        return value
