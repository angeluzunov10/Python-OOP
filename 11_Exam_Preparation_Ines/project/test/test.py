from collections import deque
from unittest import TestCase, main

from projecttest.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Sofia")

    def test_correct_init(self):
        self.assertEqual("Sofia", self.station.name)
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque())

    def test_if_name_length_is_less_than_3_or_equal_characters_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "gar"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_if_new_arriving_train_is_added_to_station(self):
        self.station.new_arrival_on_board("from Varna")
        self.assertEqual(deque(["from Varna"]), self.station.arrival_trains)

    def test_if_arrival_train_is_not_at_first_place_returns_message(self):
        self.station.arrival_trains = deque(["from Varna", "from Burgas"])
        result = self.station.train_has_arrived("from Burgas")

        self.assertEqual(f"There are other trains to arrive before from Burgas.", result)

    def test_if_arrival_train_is_on_turn(self):
        self.station.arrival_trains = deque(["from Varna", "from Burgas"])
        result = self.station.train_has_arrived("from Varna")

        self.assertEqual("from Varna is on the platform and will leave in 5 minutes.", result)

    def test_if_departure_train_is_not_at_first_place_returns_message(self):
        self.station.departure_trains = deque(["to Varna", "to Burgas"])
        result = self.station.train_has_left("to Burgas")

        self.assertEqual(False, result)

    def test_if_departure_train_is_on_turn(self):
        self.station.departure_trains = deque(["to Varna", "to Burgas"])
        result = self.station.train_has_left("to Varna")

        self.assertEqual(True, result)
        self.assertEqual(deque(["to Burgas"]), self.station.departure_trains)


if __name__ == '__main__':
    main()