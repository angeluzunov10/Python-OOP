from unittest import TestCase, main

from project1.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 100)

    def test_default_fuel_consumption_is_correct_value(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init_correct(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_driving_without_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_driving_with_fuel_decreases_fuel_with_needed(self):
        self.vehicle.drive(20)
        self.assertEqual(75, self.vehicle.fuel)

    def test_refueling_with_too_much_fuel_raises_exception(self):
        self.vehicle.fuel = 80
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(90)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refueling_with_valid_amount_adds_fuel_to_capacity(self):
        self.vehicle.fuel = 70
        self.vehicle.refuel(10)
        self.assertEqual(80, self.vehicle.fuel)

    def test_string_dunder_returns_string(self):
        self.assertEqual("The vehicle has 100 horse power with "
                         "100 fuel left and 1.25 fuel consumption",
                         self.vehicle.__str__())


if __name__ == '__main__':
    main()