from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, self.CAPACITY)

    @property
    def type(self) -> str:
        return "Secondary Service"