from abc import ABC, abstractmethod
class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass

class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I'm working!!")

class SuperWorker(Worker):
    @staticmethod
    def work():
        print("I work very hard")

class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f"`worker` must be of type {BaseWorker}")

        self.worker = worker

    def manage(self):
        if not self.worker:
            raise ValueError("You dont have any workers!")

        self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()

manager.set_worker(super_worker)
manager.manage()







