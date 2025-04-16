from locust import task, TaskSet
from flask_app_tasks.base import BaseBehavior

class AdminUserBehavior(TaskSet, BaseBehavior):
    @task
    def manage_items(self):
        token = self.login("admin", "admin123")
        if token:
            headers = {"Authorization": f"Bearer {token}"}

            # Create item
            res = self.client.post("/items", json={"title": "New Item", "content": "From admin"}, headers=headers)
            if res.status_code == 201:
                item_id = res.json()["id"]
                # Update item
                self.client.put(f"/items/{item_id}", json={"title": "Updated"}, headers=headers)
                # Delete item
                self.client.delete(f"/items/{item_id}", headers=headers)