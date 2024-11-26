from fastapi import status

from src.domain.producer.repository.interface import ProducerRepositoryInterface


class DeleteProducerUseCase:
    def __init__(self, producer_repository: ProducerRepositoryInterface):
        self._producer_repository = producer_repository

    async def execute(self, producer_id):
        producer = await self._producer_repository.find(producer_id)

        if len(producer) == 0:
            return {
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Producer not found"
            }
        await self._producer_repository.delete(producer_id)
        return {
            "status_code": status.HTTP_200_OK,
            "producer": []
        }

