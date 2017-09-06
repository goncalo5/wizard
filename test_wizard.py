import unittest
import wizard


class TestWizard(unittest.TestCase):

    def setUp(self):
        self.animals = {
            "bird": {"fly", "vertebrate"},
            "ant": {"insect"},
            "leon": {"vertebrate", "carnivorous"},
            "elephant": {"vertebrate"},
            "fly": {"fly"}
            }

    def test_make_new_dict(self):
        result = wizard.make_new_dict(
            animal_dict=self.animals, characteristic="vertebrate", positve=True)
        self.assertEqual(result, {
            "bird": {"fly", "vertebrate"},
            "leon": {"vertebrate", "carnivorous"},
            "elephant": {"vertebrate"}})
        result = wizard.make_new_dict(
            animal_dict=self.animals, characteristic="vertebrate", positve=False)
        self.assertEqual(result, {
            "ant": {"insect"},
            "fly": {"fly"}
            })

        result = wizard.make_new_dict(
            animal_dict=self.animals, characteristic="unknown", positve=True)
        self.assertEqual(result, {})
        result = wizard.make_new_dict(
            animal_dict=self.animals, characteristic="unknown", positve=False)
        self.assertEqual(result, self.animals)

    def test_fetch_all_characteristic(self):
        result = wizard.fetch_all_characteristic(self.animals)
        self.assertEqual(result, {"fly", "vertebrate", "carnivorous", "insect"})

        result = wizard.fetch_all_characteristic({})
        self.assertEqual(result, set())


if __name__ == '__main__':
    unittest.main()
