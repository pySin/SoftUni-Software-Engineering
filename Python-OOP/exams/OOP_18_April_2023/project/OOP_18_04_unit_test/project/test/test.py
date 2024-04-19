from project.robot import Robot
from unittest import TestCase, main

class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot("z1", "Military", 20, 22000)

    # Test initialize data
    def test_initial_data(self):
        self.assertEqual(self.robot.robot_id, "z1")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 20)
        self.assertEqual(self.robot.price, 22000)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    # Test category property
    def test_if_category_returns(self):
        category = self.robot.category
        self.assertEqual("Military", category)

    def test_if_category_rises_an_error_when_not_in_allowed(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "NonCategory"
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_if_category_reassigns_successfully(self):
        self.robot.category = "Education"
        self.assertEqual(self.robot.category, "Education")

    # Test 'price' property
    def test_if_price_returns(self):
        price = self.robot.price
        self.assertEqual(price, 22000)

    def test_if_price_rises_if_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -12
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_if_price_assigns_properly(self):
        self.robot.price = 19500
        self.assertEqual(self.robot.price, 19500)

    # Test upgrade() function
    def test_upgrade_when_component_already_upgraded(self):
        self.robot.upgrade("processor_a5", 1300)
        result = self.robot.upgrade("processor_a5", 700)
        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)

    def test_if_upgraded_component_added_to_hardware_upgrades(self):
        self.robot.upgrade("processor_a5", 700)
        self.assertEqual(self.robot.hardware_upgrades[0], "processor_a5")

    def test_successful_upgrade_message(self):
        result = self.robot.upgrade("processor_a5", 700)
        self.assertEqual(result, f'Robot {self.robot.robot_id} was upgraded with processor_a5.')

    # Test update() function
    def test_successfully_append_software_version(self):
        self.robot.update(3.12, 3)
        self.assertEqual(self.robot.software_updates[-1], 3.12)

    def test_result_of_successful_update(self):
        self.robot.update(3.12, 3)
        result = self.robot.update(3.13, 3)
        self.assertEqual(self.robot.software_updates[-1], 3.13)
        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 3.13.', result)

    def test_return_when_update_with_older_version(self):
        self.robot.update(3.12, 3)
        self.robot.available_capacity -= 3
        result = self.robot.update(3.11, 3)
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")

    # Test __gt__ (Greater Than) Overload Method
    def test_compare_robots_by_price_first_more_expensive(self):
        robot2 = Robot("z2", "Military", 20, 18000)
        self.assertEqual(self.robot > robot2,
                         f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {robot2.robot_id}.')

    def test_compare_robots_by_price_second_more_expensive(self):
        robot2 = Robot("z2", "Military", 20, 34000)
        self.assertEqual(self.robot > robot2,
                         f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {robot2.robot_id}.')

    def test_compare_robots_by_price_equal_worth(self):
        robot2 = Robot("z2", "Military", 20, 22000)
        self.assertEqual(self.robot > robot2,
                         f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {robot2.robot_id}.')

if __name__ == "__main__":
    main()



