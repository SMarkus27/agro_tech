import simplejson as json

from fastapi import status, Response

from src.infrastructure.producer.repository.postgres.repository import ProducerRepository
from src.usecase.producer.create.create import CreateProducerUseCase
from src.usecase.producer.create.create_dto import InputCreateProducerDto
from src.usecase.producer.delete.delete_producer import DeleteProducerUseCase
from src.usecase.producer.find_all.find_all import FindAllProducerUseCase
from src.usecase.producer.find_total.find_total import FindTotalProducerUseCase
from src.usecase.producer.update.update_producer import UpdateProducerUseCase
from src.usecase.producer.update.update_producer_dto import InputUpdateProducerDto


class ProducerCcntroller:

    @classmethod
    async def create(cls, producer: InputCreateProducerDto):
        producer_repository = ProducerRepository()
        producer = await CreateProducerUseCase(producer_repository).execute(producer)

        return Response(
            status_code=producer.get("status_code"),
            content=json.dumps(producer),
            headers={"Content-type": "application/json"}
        )

    @classmethod
    async def find_total(cls):
        producer_repository = ProducerRepository()
        producer = await FindTotalProducerUseCase(producer_repository).execute()

        return Response(
            status_code=producer.get("status_code"),
            content=json.dumps(producer),
            headers={"Content-type": "application/json"}
        )

    @classmethod
    async def find_all(cls):
        producer_repository = ProducerRepository()
        producer = await FindAllProducerUseCase(producer_repository).execute()

        return Response(
            status_code=producer.get("status_code"),
            content=json.dumps(producer),
            headers={"Content-type": "application/json"}
        )

    @classmethod
    async def update(cls, producer_id: str, producer: InputUpdateProducerDto):
        producer_repository = ProducerRepository()
        producer = await UpdateProducerUseCase(producer_repository).execute(producer_id, producer)
        return Response(
            status_code=producer.get("status_code"),
            content=json.dumps(producer),
            headers={"Content-type": "application/json"}
        )

    @classmethod
    async def delete(cls, producer_id: str):
        producer_repository = ProducerRepository()
        producer = await DeleteProducerUseCase(producer_repository).execute(producer_id)
        return Response(
            status_code=producer.get("status_code"),
            content=json.dumps(producer),
            headers={"Content-type": "application/json"}
        )
