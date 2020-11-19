from .tasks import Task_A,Task_B
import time

if __name__ == '__main__':
    result = Task_A.delay(25, child=True)
    # result = Task_B.delay()

    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)
    while result.status != 'SUCCESS':
        print ('Task finished? ', result.ready())
        print ('Task result: ', result.result)