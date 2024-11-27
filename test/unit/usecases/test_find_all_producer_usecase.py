from unittest.mock import Mock, patch

import pytest

from src.infrastructure.producer.repository.postgres.repository import ProducerRepository
from src.usecase.producer.find_all.find_all import FindAllProducerUseCase


@pytest.mark.asyncio
@patch.object(ProducerRepository, "find_all")
async def test_find_all_producer(find_all_patch: Mock):
    producer_repository = ProducerRepository()

    producer1 = {
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
    producer2 = {
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
        "producers": [producer1, producer2]
    }

    find_all_patch.return_value = [producer1, producer2]

    result = await FindAllProducerUseCase(producer_repository).execute()

    assert result == response
    assert len(result.get("producers")) == 2


@pytest.mark.asyncio
@patch.object(ProducerRepository, "find_all")
async def test_find_all_producer_none_producer(find_all_patch: Mock):
    producer_repository = ProducerRepository()
    find_all_patch.return_value = []

    response = {
        "status_code": 404,
        "producers": []
    }

    result = await FindAllProducerUseCase(producer_repository).execute()

    assert result == response
