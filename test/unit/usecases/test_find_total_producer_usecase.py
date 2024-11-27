from unittest.mock import Mock, patch

import pytest

from src.infrastructure.producer.repository.postgres.repository import ProducerRepository
from src.usecase.producer.find_total.find_total import FindTotalProducerUseCase


@pytest.mark.asyncio
@patch.object(ProducerRepository, "find_total")
async def test_find_all_producer(find_total_patch: Mock):
    producer_repository = ProducerRepository()

    total = [{
        "total_area": 5000,
        "total_farm": 2,

    }]
    response = {
        "status_code": 200,
        "total_area": 5000,
        "total_farm": 2,
    }

    find_total_patch.return_value = total

    result = await FindTotalProducerUseCase(producer_repository).execute()

    assert result == response


@pytest.mark.asyncio
@patch.object(ProducerRepository, "find_total")
async def test_find_total_producer_none_producer(find_total_patch: Mock):
    producer_repository = ProducerRepository()
    find_total_patch.return_value = []

    response = {
        "status_code": 404,
        "total_area": [],
        "total_farm": [],

    }

    result = await FindTotalProducerUseCase(producer_repository).execute()

    assert result == response
