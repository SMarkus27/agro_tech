from fastapi import status

from src.domain.producer.repository.interface import ProducerRepositoryInterface


class FindTotalProducerUseCase:
    def __init__(self, producer_repository: ProducerRepositoryInterface):
        self._producer_repository = producer_repository

    async def execute(self):
        producer = await self._producer_repository.find_total()

        if len(producer) == 0:
            return {
                "status_code": status.HTTP_404_NOT_FOUND,
                "total_area": [],
                "total_farm": [],

            }

        total_area = float(producer[0].get("total_area"))
        total_farm = float(producer[0].get("total_farm"))

        return {
                "status_code": 200,
                "total_area": total_area,
                "total_farm": total_farm,

        }
