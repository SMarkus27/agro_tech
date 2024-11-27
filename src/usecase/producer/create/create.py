from fastapi import status

from src.domain.producer.factory.factory import ProducerFactory
from src.domain.producer.repository.interface import ProducerRepositoryInterface
from src.usecase.producer.create.create_dto import InputCreateProducerDto, OutputCreateProducerDto


class CreateProducerUseCase:
    _producer_repository: ProducerRepositoryInterface

    def __init__(self, producer_repository: ProducerRepositoryInterface):
        self._producer_repository = producer_repository

    async def execute(self, data: InputCreateProducerDto) -> OutputCreateProducerDto:
        producer = ProducerFactory.create(data)
        await self._producer_repository.create(producer)

        return {
            "status_code": status.HTTP_201_CREATED,
            "id": producer.id,
            "cpf_cnpj": producer.cpf_cnpj,
            "producer_name": producer.producer_name,
            "farm_name": producer.farm_name,
            "city": producer.city,
            "state": producer.state,
            "farm_area": producer.farm_area,
            "arable_area": producer.arable_area,
            "vegetation_area": producer.vegetation_area,
            "cultivation": producer.cultivation,
            }

