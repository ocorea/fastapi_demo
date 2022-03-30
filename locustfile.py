from locust import HttpUser, task
import random

class apiLoadTest(HttpUser):
    
    @task
    def createFactorial(self):
        number=random.uniform(1, 12)
        self.client.post("http://localhost:8000/factorial", json={'number':number})
    @task
    def getMax(self):
        self.client.get("http://localhost:8000/getmax")


