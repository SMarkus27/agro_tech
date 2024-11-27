from unittest.mock import Mock, patch

import pytest

from src.infrastructure.repository.producer.postgres.repository import ProducerRepository
from src.usecase.producer.create.create import CreateProducerUseCase


@pytest.mark.asyncio
@patch.object(ProducerRepository, "create")
async def test_create_producer(create_patch: Mock):
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

    response = {
        "status_code": 201,
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

    create_patch.return_value = response

    result = await CreateProducerUseCase(producer_repository).execute(producer)

    assert result.get("status_code") == 201
    assert result.__contains__("id")


