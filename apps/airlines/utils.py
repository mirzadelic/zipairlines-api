from decimal import Decimal

from django.conf import settings


class AirplaneUtils(object):

    def __init__(self, airplane):
        self.airplane = airplane

    @property
    def tank_capacity(self):
        return Decimal(self.airplane['id']) * Decimal(settings.TANK_LITERS)

    @property
    def per_passenger_consumption(self):
        return Decimal(self.airplane['passengers']) * Decimal(
            settings.FUEL_BY_PASSENGER)

    @property
    def airplane_consumption(self):
        return Decimal(self.airplane['id']) * Decimal(
            settings.MULTIPLIED_VALUE)

    @property
    def per_minute_fuel_consumption(self):
        return self.airplane_consumption + self.per_passenger_consumption

    @property
    def max_fly_minutes(self):
        return self.tank_capacity / self.per_minute_fuel_consumption
