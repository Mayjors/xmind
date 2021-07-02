import unittest

from manager import user_manager
from model.models.user import UserSecurityTab


class UserTest(unittest.TestCase):
	def test_login(self):
		login_data = UserSecurityTab.objects.filter(delete_time=0).first()
		data = {
			'name': login_data.user_name,
			'password': login_data.password
		}
		user_manager.login(**data)
