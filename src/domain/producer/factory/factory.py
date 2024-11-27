from uuid import uuid4

from src.domain.producer.entity.entity import Producer
from src.usecase.producer.create.create_dto import InputCreateProducerDto


class ProducerFactory:

    @classmethod
    def create(cls, data: InputCreateProducerDto) -> Producer:
        return Producer(str(uuid4()),
                        data.get("cpf_cnpj"),
                        data.get("document_type"),
                        data.get("producer_name"),
                        data.get("farm_name"),
                        data.get("city"),
                        data.get("state"),
                        data.get("farm_area"),
                        data.get("arable_area"),
                        data.get("vegetation_area"),
                        data.get("cultivation"))
