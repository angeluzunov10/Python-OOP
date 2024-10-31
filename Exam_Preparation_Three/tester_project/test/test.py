from unittest import TestCase, main

from projecttest.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.trip = Trip(10000, 2, True)
        self.trip.booked_destinations_paid_amounts = {}

    def test_correct_init(self):
        self.assertEqual(self.trip.budget, 10000)
        self.assertEqual(self.trip.travelers, 2)
        self.assertEqual(self.trip.is_family, True)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {})

    def test_travellers_are_less_than_1_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_travellers_are_less_than_2_and_is_family_is_set_to_True_sets_is_family_to_False(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertEqual(False, self.trip.is_family)

    def test_if_destination_not_in_mentioned_prices_returns_message(self):
        expected_result = 'This destination is not in our offers, please choose a new one!'
        result = self.trip.book_a_trip("Italy")
        self.assertEqual(result, expected_result)

    def test_if_budget_is_less_than_the_required_price_returns_message(self):
        self.trip.budget = 1000
        expected_result = 'Your budget is not enough!'
        result = self.trip.book_a_trip("Australia")

        self.assertEqual(result, expected_result)

    def test_if_budget_is_successfully_booked(self):
        result = self.trip.book_a_trip("Bulgaria")
        expected_result = f'Successfully booked destination Bulgaria! Your budget left is 9100.00'

        self.assertEqual(result, expected_result)
        self.assertEqual({"Bulgaria": 900}, self.trip.booked_destinations_paid_amounts)

    def test_empty_booked_destinations_paid_amounts_returns_message(self):
        self.trip.booked_destinations_paid_amounts = {}
        expected_result = "No bookings yet. Budget: 10000.00"
        self.assertEqual(expected_result, self.trip.booking_status())

    def test_booking_status_on_some_booked_destinations_returns_status(self):
        self.trip.budget = 20000
        self.trip.travelers = 2
        self.trip.is_family = False
        self.trip.book_a_trip("Bulgaria")
        self.trip.book_a_trip("New Zealand")
        # self.trip.booked_destinations_paid_amounts = {
        #     "Bulgaria": 1000,
        #     "New Zealand": 15000
        # }

        result = self.trip.booking_status()
        expected_result = "Booked Destination: Bulgaria\n" \
                          "Paid Amount: 1000.00\n" \
                          "Booked Destination: New Zealand\n" \
                          "Paid Amount: 15000.00\n" \
                          "Number of Travelers: 2\n" \
                          "Budget Left: 4000.00" \

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()