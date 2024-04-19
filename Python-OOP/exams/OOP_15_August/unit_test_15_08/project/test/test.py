from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self):
        self.new_trip = Trip(1200.50, 2, True)

    # Test Initialization
    def test_init_data(self):
        self.assertEqual(self.new_trip.budget, 1200.50)
        self.assertEqual(self.new_trip.travelers, 2)
        self.assertEqual(self.new_trip.is_family, True)
        self.assertEqual(self.new_trip.booked_destinations_paid_amounts, {})

    def test_if_travelers_property_returns(self):
        number_of_travelers = self.new_trip.travelers
        self.assertEqual(2, number_of_travelers)

    def test_if_travelers_property_can_be_assigned(self):
        self.new_trip.travelers = 4
        self.assertEqual(self.new_trip.travelers, 4)

    def test_if_zero_travelers_rises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.new_trip.travelers = 0
        self.assertEqual("At least one traveler is required!", str(ve.exception))

    def test_if_is_family_returns_properly(self):
        self.assertEqual(self.new_trip.is_family, True)
        self.new_trip.is_family = False
        self.assertEqual(self.new_trip.is_family, False)

    # Test the if_family setter works properly
    def test_if_is_family_changes_to_false_with_less_two_travelers(self):
        self.new_trip.travelers = 1
        self.new_trip.is_family = True
        self.assertEqual(self.new_trip.is_family, False)
        self.new_trip.is_family = False
        self.assertEqual(self.new_trip.is_family, False)

    # Test book_a_trip() function
    def test_if_destination_in_list_of_allowed(self):
        wrong_destination = self.new_trip.book_a_trip("Florida")
        self.assertEqual("This destination is not in our offers, please choose a new one!",
                         wrong_destination)

    def test_if_budget_is_not_enough(self):
        result = self.new_trip.book_a_trip("Australia")
        self.assertEqual("Your budget is not enough!", result)

    def test_family_discount_in_book_a_trip(self):
        self.new_trip.budget = 950
        result = self.new_trip.book_a_trip("Bulgaria")
        self.assertEqual(result, f'Successfully booked destination Bulgaria! Your budget left is {50:.2f}')

    # Test booking_status() function
    def test_if_no_bookings(self):
        result = self.new_trip.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: {1200.50:.2f}')

    def test_bookings_data_in_string(self):
        self.new_trip.budget = 30000
        self.new_trip.book_a_trip("Bulgaria")
        self.new_trip.book_a_trip("Australia")
        # print(self.new_trip.booked_destinations_paid_amounts)
        c_result = self.new_trip.booking_status()
        bookings_info = """Booked Destination: Australia
Paid Amount: 10260.00
Booked Destination: Bulgaria
Paid Amount: 900.00
Number of Travelers: 2
Budget Left: 18840.00"""
        self.assertEqual(c_result, bookings_info)



if __name__ == "__main__":
    main()
