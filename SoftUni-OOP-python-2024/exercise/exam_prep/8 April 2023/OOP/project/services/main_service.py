from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name):
        super(MainService, self).__init__(name, capacity=self.CAPACITY)

    def details(self):
        return f"{self.name} Main Service:\nRobots: {', '.join([r.name for r in self.robots]) if self.robots else 'none'}"
