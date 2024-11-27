from unittest.mock import Mock, patch

import pytest

from src.infrastructure.repository.producer.postgres.repository import ProducerRepository
from src.usecase.producer.find_total.find_total import FindTotalProducerUseCase
from src.usecase.producer.update.update_producer import UpdateProducerUseCase


@pytest.mark.asyncio
@patch.object(ProducerRepository, "update")
@patch.object(ProducerRepository, "find")
async def test_update_producer(find_patch: Mock, update_patch: Mock):
    producer_repository = ProducerRepository()

    old_producer = {
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

    find_patch.return_value = old_producer

    new_producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910111",
        "document_type": "CNPJ",
        "producer_name": "Jane",
        "farm_name": "Jane's Farm",
        "city": "city 2",
        "state": "state 2",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Milho",
    }
    response = {
        "status_code": 200,
        "producer": new_producer
    }

    producer_id = "123456"
    update_patch.return_value = new_producer

    result = await UpdateProducerUseCase(producer_repository).execute(producer_id, new_producer)

    assert result == response


@pytest.mark.asyncio
@patch.object(ProducerRepository, "update")
@patch.object(ProducerRepository, "find")
async def test_update_producer(find_patch: Mock, update_patch: Mock):
    producer_repository = ProducerRepository()
    find_patch.return_value = []

    new_producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910111",
        "document_type": "CNPJ",
        "producer_name": "Jane",
        "farm_name": "Jane's Farm",
        "city": "city 2",
        "state": "state 2",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Milho",
    }
    response = {
        "status_code": 404,
        "message": "Producer not found"
    }

    producer_id = "123456"
    update_patch.return_value = new_producer

    result = await UpdateProducerUseCase(producer_repository).execute(producer_id, new_producer)

    assert result == response
