import pytest

from src.domain.producer.entity.entity import Producer


def test_valid_producer():
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
    result = Producer(**producer)

    assert result.document_type == "CPF"
    assert result.producer_name == "John"


def test_empty_id():
    producer = {
        "id": "",
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
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Id is required"


def test_empty_cpf_cnpj():
    producer = {
        "id": "12456",
        "cpf_cnpj": "",
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
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "CPF/CNPJ is required"


def test_invalid_cpf():
    producer = {
        "id": "12456",
        "cpf_cnpj": "123456",
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
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "CPF invalid"


def test_invalid_cnpj():
    producer = {
        "id": "12456",
        "cpf_cnpj": "123456",
        "document_type": "CNPJ",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "CNPJ invalid"


def test_empty_producer_name():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Producer Name is required"


def test_empty_farm_name():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Farm Name is required"


def test_empty_city():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "City is required"


def test_empty_state():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "",
        "farm_area": 1000,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "State is required"


def test_invalid_farm_area():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 0,
        "arable_area": 500,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Farm Area must be greater than 0"


def test_invalid_arable_area():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": -4,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Arable Area must be greater than 0"


def test_invalid_vegetable_area():
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
        "vegetation_area": -200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Vegetation Area must be greater than 0"


def test_empty_cultivation():
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
        "cultivation": "",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Cultivation type is required"


def test_invalid_total_arable_and_vegetable_area():
    producer = {
        "id": "12456",
        "cpf_cnpj": "12345678910",
        "document_type": "CPF",
        "producer_name": "John",
        "farm_name": "John's Farm",
        "city": "city 1",
        "state": "state 1",
        "farm_area": 1000,
        "arable_area": 900,
        "vegetation_area": 200,
        "cultivation": "Soja",
    }
    with pytest.raises(Exception) as error:
        Producer(**producer)

    assert str(error.value) == "Sum of Arable and Vegetation Area must be less or equal to Farn Area"
