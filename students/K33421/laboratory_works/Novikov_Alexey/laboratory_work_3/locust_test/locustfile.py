from locust import HttpUser, task, between


ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NDM4OTAzLCJpYXQiOjE2OTkzODkwNDIsImp0aSI6ImRjNThmYzBkZDgyNjQ2YjJiMGY3NjljMWNmYjRjMDJhIiwidXNlcl9pZCI6Mn0.Y8J6nidH5ku8NujnIvWZ3BaQacxeVBuc8p4ZWbGgx_I"


class MyUser(HttpUser):
    wait_time = between(0.5, 10)
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    @task
    def check_user(self):
        self.client.get("/api/survey/user/check/", headers=self.headers)

    @task
    def get_questions(self):
        self.client.get("/api/survey/questions/", headers=self.headers)

    @task
    def get_group(self):
        self.client.get("/oidc/group/", headers=self.headers)
