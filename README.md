# Python Celery & RabbitMQ Tutorial

<img src="https://i.imgur.com/LdZym5a.png">

## Basic Concepts

### Broker

The Broker (RabbitMQ) is responsible for the creation of task queues, dispatching tasks to task queues according to some routing rules, and then delivering tasks from task queues to workers.

### Consumer (Celery Workers)

The Consumer is the one or multiple Celery workers executing the tasks. You could start many workers depending on your use case.

### Result Backend

The Result Backend is used for storing the results of your tasks. However, it is not a required element, so if you do not include it in your settings, you cannot access the results of your tasks.


## Start Celery Worker

Run in the parent folder of our project folder test_celery

```celery -A test_celery worker --loglevel=info```

In another console, input the following (run in the parent folder of our project folder test_celery):

```python3.5 -m test_celery.run_tasks```

check it out 

<img src="https://i.imgur.com/mYxpJ2q.png">