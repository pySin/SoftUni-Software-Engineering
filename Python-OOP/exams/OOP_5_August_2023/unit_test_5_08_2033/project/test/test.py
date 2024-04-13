from unittest import TestCase
from project.second_hand_car import SecondHandCar


class TestCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("Toyota Aygo", "Mini", 450000, 3200.00)

    # Test initializer
    def test_initialization_data(self):
        self.assertEqual(self.car.model, "Toyota Aygo")
        self.assertEqual(self.car.car_type, "Mini")
        self.assertEqual(self.car.mileage, 450000)
        self.assertEqual(self.car.price, 3200.00)
        self.assertEqual(self.car.repairs, [])

    # Test "price" property
    def test_if_price_property_returns_value(self):
        price = self.car.price
        self.assertEqual(price, 3200.00)

    def test_if_price_property_can_get_value(self):
        self.car.price = 5000.00
        self.assertEqual(self.car.price, 5000.00)

    def test_if_price_property_rises_when_small_value(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.50
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    # Test "mileage" property
    def test_if_mileage_returns_properly(self):
        mileage = self.car.mileage
        self.assertEqual(mileage, 450000)

    def test_if_mileage_can_be_assigned(self):
        self.car.mileage = 230000
        self.assertEqual(self.car.mileage, 230000)

    def test_if_mileage_rises_when_too_low(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 20
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    # Test set_promotional_price() method
    def test_if_lower_price_is_assigned(self):
        self.car.set_promotional_price(1400)
        self.assertEqual(self.car.price, 1400)

    def test_if_lower_price_is_assigned_returns(self):
        result = self.car.set_promotional_price(1400)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_if_function_rises_when_price_increased(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(11300)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    # Test need_repair() function
    def test_if_repair_costs_more_than_half_price(self):
        result = self.car.need_repair(2400, "Scratched door")
        self.assertEqual("Repair is impossible!", result)

    def test_if_repair_increases_price(self):
        self.car.need_repair(400, "Scratched door")
        self.assertEqual(3600.00, self.car.price)

    def test_if_appends_repairs_description(self):
        self.car.need_repair(400, "Scratched door")
        self.assertEqual(self.car.repairs[0], "Scratched door")

    def test_success_phrase_after_repair(self):
        result = self.car.need_repair(400, "Scratched door")
        self.assertEqual("Price has been increased due to repair charges.", result)

    # Test __gt__ (Grater Then) function overload
    def test_if_gt_cant_compare_cars_of_different_types(self):
        car2 = SecondHandCar("Tesla", "S", 450000, 3200.00)
        self.assertEqual("Cars cannot be compared. Type mismatch!", self.car > car2)

    def test_if_cars_compare_properly(self):
        car2 = SecondHandCar("Tesla", "Mini", 450000, 3500.00)
        self.assertEqual(False, self.car > car2)

    # Test __str__ function overload
    # ("Toyota Aygo", "Mini", 450000, 3200.00)
    def test_if_str_return_proper_message(self):
        result_message = f"""Model Toyota Aygo | Type Mini | Milage 450000km
Current price: 3200.00 | Number of Repairs: 0"""
        self.assertEqual(result_message, self.car.__str__())




