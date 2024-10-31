from unittest import TestCase, main

from project1.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            "Mountain",
            "Helper",
            100,
            200
        )

        self.robot_with_installed_software = ClimbingRobot(
            "Mountain",
            "Helper",
            100,
            200
        )
        self.robot_with_installed_software.installed_software = [
            {"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 49},
            {"name": "Clion", "capacity_consumption": 49, "memory_consumption": 51}
        ]

    def test_correct_init(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Helper", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_create_robot_with_invalid_category_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid"

        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_create_robot_with_valid_category_returns_real_value(self):
        self.assertEqual("Mountain", self.robot.category)

    def test_get_used_capacity_consumption_for_installed_software(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_used_capacity()

        self.assertEqual(result, expected_result)

    def test_get_available_capacity(self):
        expected_result = self.robot.capacity - \
                             self.robot_with_installed_software.get_used_capacity()
        result = self.robot_with_installed_software.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_get_used_memory_for_installed_software(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory(self):
        expected_result = self.robot.memory - \
                             self.robot_with_installed_software.get_used_memory()
        result = self.robot_with_installed_software.get_available_memory()

        self.assertEqual(expected_result, result)

    def test_install_software_with_max_equal_values_expect_success(self):
        result = self.robot.install_software({"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200})

        self.assertEqual(f"Software 'PyCharm' successfully installed on Mountain part.", result)

        self.assertEqual(self.robot.installed_software, [{"name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200}])

    def test_install_software_with_less_than_max_values_expect_success(self):
        result = self.robot.install_software(
            {"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 20})

        self.assertEqual(f"Software 'PyCharm' successfully installed on Mountain part.", result)

        self.assertEqual(self.robot.installed_software,
                         [{"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 20}])

    def test_install_software_with_one_value_greater_than_max_values_returns_error(self):
        result = self.robot.install_software({"name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 1000})

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Mountain part.", result)

        self.assertEqual(self.robot.installed_software, [])

    def test_install_software_with_other_value_greater_than_max_values_returns_error(self):
        result = self.robot.install_software({"name": "PyCharm", "capacity_consumption": 1000, "memory_consumption": 10})

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Mountain part.", result)

        self.assertEqual(self.robot.installed_software, [])

if __name__ == '__main__':
    main()