from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Pier", 0.12)

    # Test initialize data
    def test_initial_data(self):
        self.assertEqual(self.driver.name, "Pier")
        self.assertEqual(self.driver.money_per_mile, 0.12)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    # Test earned_money property
    def test_if_earned_money_returns(self):
        money = self.driver.earned_money
        self.assertEqual(money, 0)

    def test_if_earned_money_can_be_assigned(self):
        self.driver.earned_money = 5
        self.assertEqual(self.driver.earned_money, 5)

    def test_if_earned_money_less_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -2
        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    # Test add_cargo_offer() function
    def test_if_add_cargo_offer_adds_location(self):
        self.driver.add_cargo_offer("Paris", 820)
        self.assertEqual(self.driver.available_cargos["Paris"], 820)

    def test_if_add_cargo_offer_adds_and_returns(self):
        result = self.driver.add_cargo_offer("Paris", 820)
        self.assertEqual(f"Cargo for 820 to Paris was added as an offer.", result)

    def test_if_add_cargo_offer_rises_when_cargo_already_available(self):
        self.driver.add_cargo_offer("Paris", 820)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Paris", 820)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    # Test drive_best_cargo_offer() function
    def test_drive_best_cargo_offer_no_offer(self):
        # print(self.driver.available_cargos)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_success_message(self):
        self.driver.add_cargo_offer("Paris", 820)
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual(f"Pier is driving 820 to Paris.", result)

    def test_drive_best_cargo_offer_miles_check(self):
        self.driver.add_cargo_offer("Paris", 820)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(self.driver.miles, 820)

    def test_drive_best_cargo_offer_money_calculation(self):
        self.driver.add_cargo_offer("Paris", 820)
        self.driver.drive_best_cargo_offer()
        self.assertEqual(38.40, round(self.driver.earned_money, 2))

    # Test check_for_activities() function
    def test_if_check_for_activities_returns_none(self):
        self.driver.earned_money = 600
        result = self.driver.check_for_activities(820)
        self.assertIsNone(result)

    # Test eat() function
    def test_if_money_decrease_when_eat(self):
        self.driver.earned_money = 40
        self.driver.eat(250)
        self.assertEqual(self.driver.earned_money, 20)

    # Test sleep() function
    def test_sleep_decreases_money(self):
        self.driver.earned_money = 60
        self.driver.sleep(2000)
        self.assertEqual(self.driver.earned_money, 15)

    # Test pump_gas() function
    def test_pump_gas_decreases_money(self):
        self.driver.earned_money = 501
        self.driver.pump_gas(3000)
        self.assertEqual(self.driver.earned_money, 1)

    # Test repair_truck function()
    def test_repair_truck_decrease_money(self):
        self.driver.earned_money = 7501
        self.driver.repair_truck(20000)
        self.assertEqual(self.driver.earned_money, 1)

    # Test __repr__ Overload
    def test_repr_expression(self):
        self.driver.add_cargo_offer("Paris", 820)
        self.driver.add_cargo_offer("Berlin", 720)
        self.driver.drive_best_cargo_offer()
        del self.driver.available_cargos["Paris"]
        self.driver.drive_best_cargo_offer()
        self.assertEqual(f"Pier has 1540 miles behind his back.", repr(self.driver))


if __name__ == "__main__":
    main()
