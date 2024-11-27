from asyncio import run

from src.infrastructure.producer.repository.postgres.connection import PostgresSQLConnection


async def create_producer_table():
    connection = await PostgresSQLConnection.get_client()
    cursor = connection.cursor()
    await cursor.execute(
        """CREATE TABLE IF NOT EXISTS producer(id VARCHAR(50), cpf_cnpj VARCHAR(14), producer_name VARCHAR(50),
                                    farm_name VARCHAR(50), city VARCHAR(50), state VARCHAR(50), farm_area decimal(5,2),
                                    arable_area decimal(5,2),vegetation_area decimal(5,2),cultivation VARCHAR(10))"""
    )
    await connection.commit()
    await cursor.close()
    await connection.close()


if __name__ == "__main__":
    run(create_producer_table())