import unittest

from manager import activity_manager


class ActivityTest(unittest.TestCase):
	def test_list(self):
		data = activity_manager.get_activity(1)
		self.assertIsNotNone(data)
