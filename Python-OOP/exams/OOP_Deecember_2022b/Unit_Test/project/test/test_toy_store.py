from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    # Test add_toy() function
    def test_add_toy_if_shelf_in_shelf_names(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "Car")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_toy_already_in_shelf(self):
        self.store.add_toy("A", "Bear")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Bear")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))
    
    def test_if_shelf_is_full(self):
        self.store.add_toy("A", "Bear")
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Car")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_if_toy_successfully_placed(self):
        self.store.add_toy("A", "Bear")
        self.assertEqual(self.store.toy_shelf["A"], "Bear")

    def test_success_toy_placement_message(self):
        result = self.store.add_toy("A", "Bear")
        self.assertEqual(f"Toy:{self.store.toy_shelf['A']} placed successfully!", result)

    # Test remove_toy() function
    def test_if_shelf_name_does_not_exists(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Egg")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_toy_not_in_shelf_given(self):
        self.store.add_toy("A", "Egg")
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Pokemon")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_if_shelf_emptied(self):
        self.store.add_toy("A", "Egg")
        self.store.remove_toy("A", "Egg")
        self.assertEqual(self.store.toy_shelf["A"], None)

    def test_successful_toy_removal_message(self):
        self.store.add_toy("A", "Egg")
        result = self.store.remove_toy("A", "Egg")
        self.assertEqual(result, f"Remove toy:Egg successfully!")


if __name__ == "__main__":
    main()




