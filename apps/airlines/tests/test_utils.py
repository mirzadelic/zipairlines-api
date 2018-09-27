from decimal import Decimal

from django.test import SimpleTestCase
from django.conf import settings

from apps.airlines.utils import AirplaneUtils


class AirplaneUtilsTests(SimpleTestCase):

    def setUp(self):
        self.airplane = {
            'id': 5,
            'passengers': 100
        }
        self.airplane_utils = AirplaneUtils(self.airplane)

    def test__tank_capacity(self):
        '''
        Test tank_capacity property
        '''

        self.assertEqual(
            self.airplane_utils.tank_capacity,
            round(Decimal(5 * 200), 3)
        )

    def test__per_passenger_consumption(self):
        '''
        Test per_passenger_consumption property
        '''

        self.assertEqual(
            self.airplane_utils.per_passenger_consumption,
            round(Decimal(100) * Decimal(0.002), 3)
        )

    def test__airplane_consumption(self):
        '''
        Test airplane_consumption property
        '''

        self.assertEqual(
            self.airplane_utils.airplane_consumption,
            round(Decimal(5) * Decimal(0.80), 3)
        )

    def test__per_minute_fuel_consumption(self):
        '''
        Test per_minute_fuel_consumption property
        '''

        self.assertEqual(
            self.airplane_utils.per_minute_fuel_consumption,
            round(
                (Decimal(5) * Decimal(0.80)) + (Decimal(100) * Decimal(0.002)),
                3
            )
        )

    def test__max_fly_minutes(self):
        '''
        Test max_fly_minutes property
        '''

        self.assertEqual(
            self.airplane_utils.max_fly_minutes,
            round(
                Decimal(5 * 200) / ((Decimal(5) * Decimal(0.80)) + (
                    Decimal(100) * Decimal(0.002))),
                3
            )
        )

    def test__fuel_required(self):
        '''
        Test fuel_required property
        '''

        for i in range(1, 10):
            airplane = {
                'id': i,
                'passengers': i*20
            }

            ap = AirplaneUtils(airplane)

            airplane_consumption = airplane['id'] * settings.MULTIPLIED_VALUE
            per_passenger_consumption = airplane['passengers'] * settings.FUEL_BY_PASSENGER

            fuel_capacity = Decimal(airplane_consumption + (
                per_passenger_consumption * airplane['passengers']))

            self.assertEqual(ap.fuel_required, round(fuel_capacity, 3))
