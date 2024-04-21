from project.climbing_robot import ClimbingRobot
import unittest


class TestClimbingRobot(unittest.TestCase):

    def setUp(self) -> None:
        self.climbing_robot = ClimbingRobot(category="Mountain", part_type="Part 1", capacity=12, memory=200)

    def test_climbing_robot_structure(self):
        self.assertEqual(ClimbingRobot.__base__.__name__, "object")
        self.assertTrue(hasattr(ClimbingRobot, "get_used_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_capacity"))
        self.assertTrue(hasattr(ClimbingRobot, "get_used_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "get_available_memory"))
        self.assertTrue(hasattr(ClimbingRobot, "install_software"))

        self.assertTrue(isinstance(getattr(ClimbingRobot, "category"), property))

    def test_initial_data(self):
        self.assertEqual("Mountain", self.climbing_robot.category)
        self.assertEqual("Part 1", self.climbing_robot.part_type)
        self.assertEqual(12, self.climbing_robot.capacity)
        self.assertEqual(200, self.climbing_robot.memory)

    def test_if_category_getter_works(self):
        category_value = self.climbing_robot.category
        self.assertEqual(category_value, self.climbing_robot.category)

    def test_if_category_setter_rises_error_for_wrong_category(self):
        with self.assertRaises(ValueError) as va:
            self.climbing_robot.category = "Non Mountain"
        self.assertEqual(f"Category should be one of {self.climbing_robot.ALLOWED_CATEGORIES}",
                         str(va.exception))

    def test_category_setter_invalid(self):
        invalid_category = 'InvalidCategory'
        with self.assertRaises(ValueError) as context:
            self.climbing_robot.category = invalid_category
        self.assertEqual(str(context.exception), f"Category should be one of {self.climbing_robot.ALLOWED_CATEGORIES}")

    def test_if_category_value_changes(self):
        self.climbing_robot.category = "Alpine"
        self.assertEqual("Alpine", self.climbing_robot.category)

    def test_category_setter_valid(self):
        valid_categories = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        for category in valid_categories:
            with self.subTest(category=category):
                self.climbing_robot.category = category
                self.assertEqual(self.climbing_robot.category, category)

    def test_get_used_capacity_with_value(self):
        self.climbing_robot.install_software({"name": "b1", "capacity_consumption": 2, "memory_consumption": 2})
        self.assertEqual(2, self.climbing_robot.get_used_capacity())

    def test_get_used_capacity(self):
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        self.climbing_robot.installed_software = [software1, software2]
        self.assertEqual(self.climbing_robot.get_used_capacity(), 70)

    def test_get_available_capacity_with_value(self):
        self.climbing_robot.install_software({"name": "b1", "capacity_consumption": 2, "memory_consumption": 2})
        self.assertEqual(10, self.climbing_robot.get_available_capacity())

    def test_get_available_capacity(self):
        self.climbing_robot.installed_software = [{'capacity_consumption': 30}]
        self.assertEqual(self.climbing_robot.get_available_capacity(), -18)

    def test_get_used_memory_with_value(self):
        self.climbing_robot.install_software({"name": "b1", "capacity_consumption": 2, "memory_consumption": 2})
        self.assertEqual(2, self.climbing_robot.get_used_memory())

    def test_get_used_memory(self):
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        self.climbing_robot.installed_software = [software1, software2]
        self.assertEqual(self.climbing_robot.get_used_memory(), 120)

    def test_get_available_memory_with_value(self):
        self.climbing_robot.install_software({"name": "b1", "capacity_consumption": 2, "memory_consumption": 2})
        self.assertEqual(198, self.climbing_robot.get_available_memory())

    def test_get_available_memory(self):
        self.climbing_robot.installed_software = [{'memory_consumption': 30}]
        self.assertEqual(self.climbing_robot.get_available_memory(), 170)

    def test_install_software_success_return(self):
        success_text = self.climbing_robot.install_software({"name": "b1", "capacity_consumption": 2,
                                                             "memory_consumption": 2})
        self.assertEqual(f"Software 'b1' successfully installed on Mountain part.",
                         success_text)

    def test_install_software_exact_capacity_memory(self):
        software = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        self.climbing_robot.installed_software = []
        self.climbing_robot.capacity = software['capacity_consumption']
        self.climbing_robot.memory = software['memory_consumption']

        result = self.climbing_robot.install_software(software)

        expected_message = f"Software '{software['name']}' successfully installed on {self.climbing_robot.category} part."
        self.assertEqual(result, expected_message)
        self.assertEqual(self.climbing_robot.installed_software, [software])

    def test_install_software_failure(self):
        failure_text = self.climbing_robot.install_software({"name": "b1", "capacity_consumption": 2,
                                                             "memory_consumption": 202})
        self.assertEqual("Software 'b1' cannot be installed on Mountain part.", failure_text)


if __name__ == "__main__":
    unittest.main()
