import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(0.5, 5)
    
    @task
    def hello_self(self):
        self.client.get("/hello/myName")
    
    
    @task(5)
    def hello_random(self):
        self.client.get("/hello/random")
            
            
    @task(5)
    def primes(self):
        counts = [10, 50, 100, 500, 1000]
        for c in counts:
            self.client.get("/primes/" + str(c))
            
    @task
    def does_not_exist(self):
        with self.client.get("/does_not_exist/", catch_response=True) as response:
            if response.status_code == 404:
                response.success()
