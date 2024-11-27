from abc import ABCMeta, abstractmethod


class RepositoryInterface(metaclass=ABCMeta):

    @abstractmethod
    async def create(self, producer):
        pass

    @abstractmethod
    async def find(self, id: str):
        pass

    @abstractmethod
    async def find_all(self):
        pass

    @abstractmethod
    async def find_total(self):
        pass

    @abstractmethod
    async def update(self, id: str, entity):
        pass

    @abstractmethod
    async def delete(self, id: str) -> None:
        pass
