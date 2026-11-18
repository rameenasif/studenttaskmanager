import unittest

import tasks


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_list = []

    def test_add_task(self):
        task = tasks.add_task(self.task_list, "Study Git")
        self.assertEqual(len(self.task_list), 2)
        self.assertEqual(task["title"], "Study Git")
        self.assertFalse(task["done"])

    def test_add_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            tasks.add_task(self.task_list, "   ")
        self.assertEqual(self.task_list, [])

    def test_complete_task(self):
        task = tasks.add_task(self.task_list, "Write report")
        self.assertTrue(tasks.complete_task(self.task_list, task["id"]))
        self.assertTrue(self.task_list[0]["done"])

    def test_delete_task(self):
        task = tasks.add_task(self.task_list, "Old task")
        self.assertTrue(tasks.delete_task(self.task_list, task["id"]))
        self.assertEqual(self.task_list, [])

    def test_delete_invalid_id(self):
        tasks.add_task(self.task_list, "Keep me")
        self.assertFalse(tasks.delete_task(self.task_list, 99))
        self.assertEqual(len(self.task_list), 1)


if __name__ == "__main__":
    unittest.main()