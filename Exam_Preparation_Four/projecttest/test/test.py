from unittest import TestCase, main

from projecttest.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Audi", "car", 1000, 10000)
        self.repairs = []

        self.car_from_different_type = SecondHandCar("Mercedes", "bus", 5000, 15000)
        self.car_from_different_type.repairs = []

        self.car_with_repairs = SecondHandCar("Audi", "car", 1000, 11000)
        self.car_with_repairs.repairs = ["new bumper", "new turbo"]

    def test_correct_init(self):
        self.assertEqual("Audi", self.car.model)
        self.assertEqual("car", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(10000, self.car.price)
        self.assertEqual([], self.car.repairs)
        self.assertEqual(["new bumper", "new turbo"], self.car_with_repairs.repairs)

    def test_less_than_one_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.5

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_value_less_than_100_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 50

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_greater_new_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(12000)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_smaller_new_price_returns_success(self):
        expected_result = 'The promotional price has been successfully set.'
        result = self.car.set_promotional_price(8000)

        self.assertEqual(result, expected_result)

    def test_repairing_price_is_more_than_half_of_the_car_price_returns_message(self):
        result = self.car_with_repairs.need_repair(8000, "new turbo")
        expected_result = 'Repair is impossible!'

        self.assertEqual(result, expected_result)

    def test_repairing_price_is_less_than_half_of_the_car_price_returns_success(self):
        result = self.car.need_repair(1000, "new_turbo")
        expected_result = 'Price has been increased due to repair charges.'

        self.assertEqual(result, expected_result)
        self.assertEqual(11000, self.car.price)
        self.assertEqual(["new_turbo"], self.car.repairs)

    def test_comparing_two_different_car_types_returns_message(self):
        self.car.car_type = "car"
        self.car_from_different_type.car_type = "bus"

        expected_result = 'Cars cannot be compared. Type mismatch!'
        result = self.car.__gt__(self.car_from_different_type)

        self.assertEqual(expected_result, result)

    def test_comparing_two_car_from_same_types_returns_success(self):
        result = self.car.__gt__(self.car_with_repairs)

        self.assertEqual(False, result)

    def test_string_return(self):
        result = self.car.__str__()
        expected_result = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    main()
