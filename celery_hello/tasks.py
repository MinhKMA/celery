from celery.decorators import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task(name="demo_task")
def hello():
    logger.info("Sent feedback email")
    with open('/home/minhkma/minhkma.txt', 'a') as the_file:
        the_file.write('Hello\n')
    return 1
