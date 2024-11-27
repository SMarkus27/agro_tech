from src.controller.base.controller import BaseController
from src.controller.producer.controller import ProducerCcntroller
from src.infrastructure.api.fastapi.routes.base import BaseAPIRouter
from src.usecase.producer.create.create_dto import InputCreateProducerDto
from src.usecase.producer.update.update_producer_dto import InputUpdateProducerDto

router = BaseAPIRouter.get_instance()


@router.post("/producers", tags=["producer"])
async def create(producer: InputCreateProducerDto):
    return await ProducerCcntroller.create(producer)


@router.get("/producers", tags=["producer"])
async def find_all():
    return await ProducerCcntroller.find_all()


@router.get("/producers/total", tags=["producer"])
async def find_total_area():
    return await ProducerCcntroller.find_total()


@router.put("/producers/{producer_id}", tags=["producer"])
async def update(producer_id: str, producer: InputUpdateProducerDto):
    return await ProducerCcntroller.update(producer_id, producer)


@router.delete("/producers/{producer_id}", tags=["producer"])
async def delete(producer_id):
    return await ProducerCcntroller.delete(producer_id)