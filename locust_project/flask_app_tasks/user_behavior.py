from locust import task, TaskSet
from flask_app_tasks.base import BaseBehavior


class NormalUserBehavior(TaskSet, BaseBehavior):
    @task
    def view_items(self):
        token = self.login("user", "user123")
        if token:
            headers = {"Authorization": f"Bearer {token}"}
            self.client.get("/items", headers=headers)
            self.client.get("/items/1", headers=headers)