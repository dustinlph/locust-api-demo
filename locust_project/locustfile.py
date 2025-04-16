from locust import HttpUser, between
from locust_tasks.user_behavior import NormalUserBehavior
from locust_tasks.admin_behavior import AdminUserBehavior

class NormalUser(HttpUser):
	wait_time = between(1, 2)
	tasks = [NormalUserBehavior]

class AdminUser(HttpUser):
	wait_time = between(1, 2)
	tasks = [AdminUserBehavior]