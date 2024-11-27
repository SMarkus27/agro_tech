from fastapi import status

from src.domain.producer.repository.interface import ProducerRepositoryInterface
from src.usecase.producer.update.update_producer_dto import InputUpdateProducerDto


class UpdateProducerUseCase:
    _producer_repository: ProducerRepositoryInterface

    def __init__(self, producer_repository: ProducerRepositoryInterface):
        self._producer_repository = producer_repository

    async def execute(self, producer_id: str, data: InputUpdateProducerDto):
        producer = await self._producer_repository.find(producer_id)

        if len(producer) == 0:
            return {
                "status_code": status.HTTP_404_NOT_FOUND,
                "message": "Producer not found"
            }

        updated_producer = await self._producer_repository.update(producer_id, data)
        updated_producer = updated_producer[0]
        return {
                "status_code": status.HTTP_200_OK,
                "cpf_cnpj": updated_producer.get("cpf_cnpj"),
                "updated_producer_name": updated_producer.get("updated_producer_name"),
                "farm_name": updated_producer.get("farm_name"),
                "city": updated_producer.get("city"),
                "state": updated_producer.get("state"),
                "farm_area": updated_producer.get("farm_area"),
                "arable_area": updated_producer.get("arable_area"),
                "vegetation_area": updated_producer.get("vegetation_area"),
                "cultivation": updated_producer.get("cultivation"),
            }

