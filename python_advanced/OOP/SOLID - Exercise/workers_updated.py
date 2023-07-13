from abc import ABC, abstractmethod
import time



class Workable(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass

class Eatable(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Workable, Eatable):
    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)

class SuperWorker(Workable, Eatable):
    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)

class Robot(Workable):
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass

class BreakManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, Eatable):
            raise AssertionError(f"`worker` must be of type {Eatable}")

        self.worker = worker

    def lunch_break(self):
        if not self.worker:
            raise AssertionError("You dont have worker!")

        self.worker.eat()

class WorkManager(Manager):
    def set_worker(self, worker):
        if not isinstance(worker, Workable):
            raise AssertionError(f"`worker` must be of type {Workable}")

        self.worker = worker

    def manage(self):
        if not self.worker:
            raise AssertionError("You dont have worker!")

        self.worker.work()




work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except AssertionError:
    pass


