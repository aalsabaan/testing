import random
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass
    
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get("http://localhost:5000")