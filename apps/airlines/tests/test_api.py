from decimal import Decimal

from django.conf import settings
from django.urls import reverse

from rest_framework.test import APISimpleTestCase


class AirplanesAPITests(APISimpleTestCase):

    def setUp(self):
        self.url = reverse('api:airlines:airplane')

    def test__more_than_10__failed(self):
        '''
        Sending more than 10 planes, that will raise validation error
        '''

        data = {
            'airplanes': [{'id': i, 'passengers': 3} for i in range(1, 12)]
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data['airplanes'][0], 'Max 10 planes allowed.')

    def test__success(self):
        '''
        Success data returned
        '''

        data = {
            'airplanes': [{'id': i, 'passengers': i*20} for i in range(1, 6)]
        }

        response = self.client.post(self.url, data)
        airplanes = response.data['airplanes']

        self.assertEqual(response.status_code, 200)

        for i, airplane in enumerate(airplanes):
            item = data['airplanes'][i]

            tank_capacity = round(
                Decimal(item['id'] * settings.TANK_LITERS), 3)
            per_passenger_consumption = round(
                Decimal(item['passengers'] * settings.FUEL_BY_PASSENGER), 3)
            per_minute_fuel_consumption = round(
                Decimal(item['id']) * Decimal(settings.MULTIPLIED_VALUE) + Decimal(item['passengers']) * Decimal(settings.FUEL_BY_PASSENGER),
                3
            )
            max_fly_minutes = round(
                tank_capacity / per_minute_fuel_consumption, 3)

            self.assertEqual(airplane['tank_capacity'], tank_capacity)
            self.assertEqual(
                airplane['per_passenger_consumption'],
                per_passenger_consumption
            )
            self.assertEqual(
                airplane['per_minute_fuel_consumption'], per_minute_fuel_consumption
            )
            self.assertEqual(
                airplane['max_fly_minutes'], max_fly_minutes
            )
