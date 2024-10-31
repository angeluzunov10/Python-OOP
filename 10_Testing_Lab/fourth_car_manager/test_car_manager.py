from unittest import TestCase, main

from car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.car = Car("BMW", "3-series", 10, 100)

    def test_correct_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("3-series", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_less_than_zero_value_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refueling_with_zero_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refueling_with_more_fuel_than_capacity_fills_to_capacity(self):
        self.car.fuel_capacity = 100
        self.car.refuel(110)
        self.assertEqual(100, self.car.fuel_capacity)

    def test_driving_without_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(150)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_driving_car_lowers_fuel_amount(self):
        self.car.refuel(110)
        self.car.drive(10)
        self.assertEqual(99, self.car.fuel_amount)


if __name__ == '__main__':
    main()
