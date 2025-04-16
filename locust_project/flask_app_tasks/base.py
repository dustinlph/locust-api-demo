from locust import TaskSet

class BaseBehavior:
    def login(self, username, password):
        with self.client.post("/login", json={"username": username, "password": password},catch_response=True) as response:
            if response.status_code == 200:
                print(f"[OK] {username} login success")
                return response.json()["token"]
            else:
                print(f"[FAIL] {username} login failed: {response.status_code}, {response.text}")
                response.failure("Login failed")
                return None