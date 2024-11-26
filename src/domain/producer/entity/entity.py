from dataclasses import dataclass


@dataclass
class Producer:
    id: str
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

    def __post_init__(self):
        Producer.verify_id(self.id)
        Producer.verify_cpf_cnpj(self.cpf_cnpj, self.document_type)
        Producer.verify_producer_name(self.producer_name)
        Producer.verify_farm_name(self.farm_name)
        Producer.verify_city(self.city)
        Producer.verify_state(self.state)
        Producer.verify_farm_area(self.farm_area)
        Producer.verify_arable_area(self.arable_area)
        Producer.verify_vegetation_area(self.vegetation_area)
        Producer.verify_cultivation(self.cultivation)
        Producer.verify_arable_and_vegetation_area(self.arable_area, self.vegetation_area, self.farm_area)

    @staticmethod
    def verify_id(id):
        if len(id) == 0:
            raise Exception("Id is required")
        return id

    @staticmethod
    def verify_cpf_cnpj(cpf_cnpj, document_type):
        if len(cpf_cnpj) == 0:
            raise Exception("CPF/CNPJ is required")
        print(document_type)
        if document_type == "CPF" and len(cpf_cnpj) < 11:
            print("aaa")
            raise Exception("CPF invalid")
        if document_type == "CNPJ" and len(cpf_cnpj) != 14:
            raise Exception("CNPJ invalid")

    @staticmethod
    def verify_producer_name(producer_name: str) -> str:
        if len(producer_name) == 0:
            raise Exception("Producer Name is required")
        return producer_name

    @staticmethod
    def verify_farm_name(farm_name: str) -> str:
        if len(farm_name) == 0:
            raise Exception("Farm Name is required")
        return farm_name

    @staticmethod
    def verify_city(city: str) -> str:
        if len(city) == 0:
            raise Exception("City is required")
        return city

    @staticmethod
    def verify_state(state: str) -> str:
        if len(state) == 0:
            raise Exception("State is required")
        return state

    @staticmethod
    def verify_farm_area(farm_area: float) -> float:
        if farm_area <= 0:
            raise Exception("Farm Area must be greater than 0")
        return farm_area

    @staticmethod
    def verify_arable_area(arable_area: float) -> float:
        if arable_area <= 0:
            raise Exception("Arable Area must be greater than 0")
        return arable_area

    @staticmethod
    def verify_vegetation_area(vegetation_area: float) -> float:
        if vegetation_area <= 0:
            raise Exception("Vegetation Area must be greater than 0")
        return vegetation_area

    @staticmethod
    def verify_cultivation(cultivation: str) -> str:
        if len(cultivation) == 0:
            raise Exception("Cultivation type is required")
        return cultivation

    @staticmethod
    def verify_arable_and_vegetation_area(arable_area: float, vegetation: float, farm_area: float) -> bool:
        area_util = arable_area + vegetation
        if farm_area <= area_util:
            raise Exception("Sum of Arable and Vegetation Area must be less or equal to Farn Area")
        return True

