from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    @property
    def type(self) -> str:
        return "Main Service"