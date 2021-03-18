# git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
# cd microservices-demo/src/loadgenerator

# export FRONTEND_ADDR=localhost

# rename : sock shop locustfile.py   to locustfile.py
#  ./loadgen.sh

# sock shop locustfile.py  file
#  loadgen.sh is using test steps in : locustfile.py for steps





import random
from locust import HttpUser, TaskSet, between
from random import randint, choice

def index(l):

    catalogue = l.client.get("/catalogue").json()
    category_item = choice(catalogue)
    item_id = category_item["id"]
    
    l.client.get("/")
    #l.client.get("/login", {"username": "user", "password": "password"})
    l.client.get("/category.html")
    l.client.get("/detail.html?id=03fef6ac-1896-4ce8-bd69-b798f85c6e0b")
    l.client.get("/basket.html")
    l.client.delete("/cart")
    l.client.post("/cart", json={"id": item_id, "quantity": 1})
    l.client.get("/customer-orders.html?")
    l.client.get("/customer-order.html?order=/orders/6053965ab9d8210008957fe8")
    
    
class UserBehavior(TaskSet):

    def on_start(self):
        index(self)

    tasks = {index: 1}

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)
