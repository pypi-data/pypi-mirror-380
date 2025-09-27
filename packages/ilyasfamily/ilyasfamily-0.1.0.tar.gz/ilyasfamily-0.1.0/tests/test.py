import unittest
from ilyasfamily import Node, dump_file, load_file, Set, Map

class TestIlyasFamily(unittest.TestCase):
    def test_node_roundtrip(self):
        person = Node("Person", {"Name": "Budi", "Age": 21})
        dump_file(person, "person.ifamily")
        loaded = load_file("person.ifamily")
        self.assertIn("Person", str(loaded))

    def test_set_repr(self):
        s = Set([1, 2, 3])
        self.assertTrue(str(s).startswith("@set"))

    def test_map_repr(self):
        m = Map({"a": 1, "b": 2})
        self.assertTrue(str(m).startswith("@map"))

if __name__ == "__main__":
    unittest.main()
