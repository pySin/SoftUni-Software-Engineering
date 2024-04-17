from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailway(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation("SofiaRail")

    # Test Initialization
    def test_init_name_property_cen_getter(self):
        self.assertEqual("SofiaRail", self.station.name)

    def test_name_too_short_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "No"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_if_arrival_trains_var_is_type_deque(self):
        self.assertEqual("deque", self.station.arrival_trains.__class__.__name__)

    def test_if_departure_trains_var_is_type_deque(self):
        self.assertEqual("deque", self.station.departure_trains.__class__.__name__)

    # Test new_arrival_on_board_function()
    def test_new_arrival_trains_added_to_queue(self):
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        self.assertEqual(self.station.arrival_trains[-1], "Train from Burgas on way 1")

    # Test train_has_arrived() function
    def test_train_arrival_with_empty_arrivals(self):
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.assertEqual(self.station.train_has_arrived("Train from Burgas on way 1"),
                         f"There are other trains to arrive before Train from Burgas on way 1.")

    def test_train_arrival_is_the_first_on_the_queue(self):
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        arrived_train = self.station.train_has_arrived("Train from Montana on way 2")

        self.assertEqual(arrived_train, f"Train from Montana on way 2 is on the platform and will leave in 5 minutes.")

    def test_if_departure_trains_updated(self):
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        self.station.train_has_arrived("Train from Montana on way 2")

        self.assertIn("Train from Montana on way 2", self.station.departure_trains)

    # Test train_has_left_function()
    def test_train_left_successfully(self):
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.train_has_arrived("Train from Burgas on way 1")
        successful_departure = self.station.train_has_left("Train from Burgas on way 1")
        self.assertEqual(successful_departure, True)

    def test_train_left_removes_left_trains_from_departure_trains(self):
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.train_has_arrived("Train from Burgas on way 1")
        self.station.train_has_arrived("Train from Montana on way 2")
        self.station.train_has_left("Train from Burgas on way 1")
        self.assertNotIn("Train from Burgas on way 1", self.station.departure_trains)

    def test_train_left_is_not_first_in_queue(self):
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.train_has_arrived("Train from Burgas on way 1")
        self.station.train_has_arrived("Train from Montana on way 2")
        wrong_train = self.station.train_has_left("Train from Montana on way 2")
        self.assertEqual(wrong_train, False)

    def test_if_train_not_left_keeps_queue_the_same(self):
        self.station.new_arrival_on_board("Train from Burgas on way 1")
        self.station.new_arrival_on_board("Train from Montana on way 2")
        self.station.train_has_arrived("Train from Burgas on way 1")
        self.station.train_has_arrived("Train from Montana on way 2")
        self.station.train_has_left("Train from Montana on way 2")
        self.assertEqual(len(self.station.departure_trains), 2)




if __name__ == "__main__":
    main()

