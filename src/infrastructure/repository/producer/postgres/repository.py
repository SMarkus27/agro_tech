from src.domain.producer.entity.entity import Producer
from src.domain.producer.repository.interface import ProducerRepositoryInterface
from src.infrastructure.repository.producer.postgres.connection import PostgresSQLConnection
from src.usecase.producer.update.update_producer_dto import InputUpdateProducerDto


class ProducerRepository(ProducerRepositoryInterface):

    @classmethod
    async def create(cls, producer: Producer) -> dict:
        producer = producer.__dict__
        query = (
            f"""INSERT INTO producer (id, cpf_cnpj, producer_name,
                                    farm_name, city, state, farm_area,
                                    arable_area, vegetation_area, cultivation)
            VALUES ('{producer['id']}', '{producer['cpf_cnpj']}', '{producer['producer_name']}',
                    '{producer['farm_name']}','{producer['city']}','{producer['state']}',
                    {producer['farm_area']}, {producer['arable_area']},
                    {producer['vegetation_area']},'{producer['cultivation']}') 
            RETURNING *"""
        )
        return await PostgresSQLConnection.execute_query(query, True)

    @classmethod
    async def find(cls, producer_id: str):
        query = f"SELECT * FROM producer WHERE id = '{producer_id}'"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find_all(cls):
        query = "SELECT * FROM producer"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def find_total(cls):
        query = "SELECT SUM(farm_area) as total_area, COUNT(id) as total_farm FROM producer"
        result = await PostgresSQLConnection.execute_query(query)
        return result

    @classmethod
    async def update(cls, producer_id: str, producer: InputUpdateProducerDto):
        query = (
            f"UPDATE producer SET producer_name='{producer['producer_name']}',"
            f"cpf_cnpj='{producer['cpf_cnpj']}',"
            f"farm_name='{producer['farm_name']}',"
            f"city='{producer['city']}',"
            f"state='{producer['state']}',"
            f"farm_area= {producer['farm_area']},"
            f"arable_area= {producer['arable_area']},"
            f"vegetation_area= {producer['vegetation_area']},"
            f"cultivation='{producer['cultivation']}'"
            f"WHERE id='{producer_id}' RETURNING *"
        )
        result = await PostgresSQLConnection.execute_query(query, True)
        return result

    @classmethod
    async def delete(cls, producer_id: str):
        query = f"DELETE FROM producer WHERE id ='{producer_id}' RETURNING *"
        result = await PostgresSQLConnection.execute_query(query, True)
        return result


