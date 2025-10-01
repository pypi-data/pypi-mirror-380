# tests/test_utils.py
import unittest
import importlib

MODULE_PATH = "opticedge_cloud_utils.dict"  # adjust if deep_merge is in another file/module


class TestDeepMerge(unittest.TestCase):
    def setUp(self):
        if MODULE_PATH in globals():
            globals().pop(MODULE_PATH)
        self.module = importlib.import_module(MODULE_PATH)

    def tearDown(self):
        importlib.reload(self.module)

    def test_merges_non_overlapping_keys(self):
        base = {"a": 1}
        updates = {"b": 2}
        result = self.module.deep_merge(base, updates)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_overwrites_existing_value(self):
        base = {"a": 1, "b": 2}
        updates = {"b": 99}
        result = self.module.deep_merge(base, updates)
        self.assertEqual(result, {"a": 1, "b": 99})

    def test_deep_merges_nested_dicts(self):
        base = {"a": {"x": 1, "y": 2}}
        updates = {"a": {"y": 99, "z": 3}}
        result = self.module.deep_merge(base, updates)
        self.assertEqual(result, {"a": {"x": 1, "y": 99, "z": 3}})

    def test_removes_key_when_value_none_and_delete_nulls_true(self):
        base = {"a": 1, "b": 2}
        updates = {"b": None}
        result = self.module.deep_merge(base, updates, delete_nulls=True)
        self.assertEqual(result, {"a": 1})

    def test_preserves_none_when_delete_nulls_false(self):
        base = {"a": 1, "b": 2}
        updates = {"b": None}
        result = self.module.deep_merge(base, updates, delete_nulls=False)
        self.assertEqual(result, {"a": 1, "b": None})

    def test_handles_empty_updates(self):
        base = {"a": 1}
        updates = {}
        result = self.module.deep_merge(base, updates)
        self.assertEqual(result, {"a": 1})

    def test_handles_empty_base(self):
        base = {}
        updates = {"x": 10}
        result = self.module.deep_merge(base, updates)
        self.assertEqual(result, {"x": 10})

    def test_original_base_not_modified(self):
        base = {"a": {"b": 1}}
        updates = {"a": {"c": 2}}
        result = self.module.deep_merge(base, updates)
        self.assertNotEqual(id(result), id(base))
        self.assertEqual(result, {"a": {"b": 1, "c": 2}})
        self.assertEqual(base, {"a": {"b": 1}})  # unchanged


if __name__ == "__main__":
    unittest.main()
