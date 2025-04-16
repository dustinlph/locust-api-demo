from locust import HttpUser, between
from flask_app_tasks.user_behavior import NormalUserBehavior
from flask_app_tasks.admin_behavior import AdminUserBehavior

class NormalUser(HttpUser):
	wait_time = between(1, 2)
	tasks = [NormalUserBehavior]

class AdminUser(HttpUser):
	wait_time = between(1, 2)
	tasks = [AdminUserBehavior]