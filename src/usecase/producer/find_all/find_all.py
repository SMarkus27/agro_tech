from fastapi import status

from src.domain.producer.repository.interface import ProducerRepositoryInterface


class FindAllProducerUseCase:
    def __init__(self, producer_repository: ProducerRepositoryInterface):
        self._producer_repository = producer_repository

    async def execute(self):
        producer = await self._producer_repository.find_all()

        if len(producer) == 0:
            return {
                "status_code": status.HTTP_404_NOT_FOUND,
                "producers": []
            }
        return {
                "status_code": 200,
                "producers": producer
        }
