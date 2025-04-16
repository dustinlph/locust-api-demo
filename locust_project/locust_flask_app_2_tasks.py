# coding=utf-8
"""
@Project: locust-drill
@File: /locust_demo.py
@Author: Dustin Lin
@Created on: 2022/8/11 11:14:32
"""
from locust import HttpUser, TaskSet, task, constant_throughput, SequentialTaskSet
from locust.runners import logger
from datetime import datetime

"""
* Command of run with Web UI
===============================
Master:
locust -f locust_demo.py --master
Worker(*N):
locust -f locust_demo.py --worker --master-host=127.0.0.1
parameter:  --logfile=locust.log
Web UI:
http://localhost:8089/
===============================
* No Web UI & only 1 worker
locust -f locust_demo.py --headless  --users 1 -r 1 -t 5
-f: Filename
--headless: No Web UI
--users:  User amount
-r: hatch rate
-t: running time
===============================
* Run with config file
locust --config=conf/demo.conf
!! Set the argument(expect-workers), Locust will wait till current worker amounts same as setting!!
locust -f locust_demo.py --worker --master-host=127.0.0.1
"""


class GeneralTaskSetDemo(TaskSet):
    def on_start(self):
        logger.info('Worker started a TaskSet')

    def on_stop(self):
        logger.info('Worker stopped a TaskSet')

    @task(1)
    def index(self):
        self.client.request(
            method='GET',
            url='/'
        )
        # self.client.get('/')

    def test1(self):
        self.client.request(
            method='GET',
            url='/test1'
        )

    def post(self):
        response = self.client.request(
            method='POST',
            url='/post',
            json={"test": "123"}
        )
        logger.info(f"Status Code: {response.status_code}; Body: {response.content}")

    @task(4)
    def go_run_post_test1(self):
        self.index()
        self.post()
        self.test1()

    # tasks = {test1: 2, post: 1}
    # tasks = [test1, post]
    # User dict. can set the func weight
    # User list, the weight is 1:1


class SequentialTaskSetDemo(SequentialTaskSet):
    """
    The order is according to the task radio and the function order:
    order: test2 -> test3 -> test3 -> test3 -> test3 -> test3 -> test1 -> test1 -> test1
    """

    def on_start(self):
        logger.info("first go here: on_start")

    def on_stop(self):
        logger.info("final go hear: on_stop")

    @task(1)
    def test2(self):
        self.client.request(
            method='GET',
            url='/test2'
        )
        logger.info("test2")

    @task(5)
    def test3(self):
        self.client.request(
            method='GET',
            url='/test3'
        )
        logger.info("test3")

    @task(3)
    def test1(self):
        self.client.request(
            method='GET',
            url='/test1'
        )
        logger.info("test1")


class TestWaitFuncTime(TaskSet):
    def on_start(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y %H:%M:%S")
        print(f"on_start: {date_time}")

    @task(1)
    def test1(self):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y %H:%M:%S")
        print(f"test1: {date_time}")


class WebsiteUser(HttpUser):
    host = 'http://127.0.0.1:7777'
    task_set = task(GeneralTaskSetDemo)
    wait_time = constant_throughput(0.2)

    def on_start(self):
        # Called when a worker start a task
        logger.info("Create a worker")

    def on_stop(self):
        # Called when a worker stop a task
        logger.info("Kill a worker")