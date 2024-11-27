from typing_extensions import TypedDict


class InputCreateProducerDto(TypedDict):
    cpf_cnpj: str
    document_type: str
    producer_name: str
    farm_name: str
    city: str
    state: str
    farm_area: float
    arable_area: float
    vegetation_area: float
    cultivation: str


class OutputCreateProducerDto(TypedDict):
    id: str
    cpf_cnpj: str
    producer_name: str
    farm_name: str
    city: str
    state: str
    farm_area: float
    arable_area: float
    vegetation_area: float
    cultivation: str






