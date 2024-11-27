from unittest.mock import Mock, patch

import pytest

from src.infrastructure.repository.producer.postgres.repository import ProducerRepository
from src.usecase.producer.delete.delete_producer import DeleteProducerUseCase


@pytest.mark.asyncio
@patch.object(ProducerRepository, "delete")
@patch.object(ProducerRepository, "find")
async def test_delete_producer(find_patch: Mock, delete_patch: Mock):
    producer_repository = ProducerRepository()

    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }

    find_patch.return_value = producer

    response = {
        "status_code": 200,
        "producer": []
    }

    producer_id = "123456"
    delete_patch.return_value = []

    result = await DeleteProducerUseCase(producer_repository).execute(producer_id)

    assert result == response


@pytest.mark.asyncio
@patch.object(ProducerRepository, "delete")
@patch.object(ProducerRepository, "find")
async def test_delete_producer(find_patch: Mock, delete_patch: Mock):
    producer_repository = ProducerRepository()
    find_patch.return_value = []

    producer_id = "123456"
    delete_patch.return_value = []

    response = {
        "status_code": 404,
        "message": "Producer not found"
    }

    result = await DeleteProducerUseCase(producer_repository).execute(producer_id)

    assert result == response
