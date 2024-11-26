from typing_extensions import TypedDict


class InputUpdateProducerDto(TypedDict):
    cpf_cnpj: str
    producer_name: str
    farm_name: str
    city: str
    state: str
    farm_area: float
    arable_area: float
    vegetation_area: float
    cultivation: str
