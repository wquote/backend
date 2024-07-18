# ToDo
# [/] venv within docker
# [X] motor_asyncio for async requests to database.
#    -> Maybe not.
# [X] ObjectId
#    -> Letting MongoDB create document ids, and tranforming them into strings
#       when reading from DB.
# [ ] criar paginação nos métodos read_all ($skip e $limit)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import auth_service
from app.customer import customer_controller
from app.decking_material_order.board import dmo_board_controller
from app.decking_material_order.finishing import dmo_finishing_controller
from app.decking_material_order.footing import dmo_footing_controller
from app.decking_material_order.frame import dmo_frame_controller
from app.decking_material_order.galvanized import dmo_galvanized_controller
from app.decking_material_order.railing import dmo_railing_controller
from app.decking_material_order.rain_scape import dmo_rain_scape_controller
from app.decking_quote import decking_quote_controller
from app.material import material_controller
from app.quote import quote_controller

app = FastAPI(title="wQuote API", version="0.0.1")

origins = [
    "http://localhost:4201",
    "http://localhost",
    "https://wquote.onrender.com",
    "https://h-wquote.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello, wQuoter!"}


app.include_router(auth_service.router)

app.include_router(customer_controller.router)
app.include_router(material_controller.router)
app.include_router(decking_quote_controller.router)
app.include_router(quote_controller.router)

app.include_router(dmo_footing_controller.router)
app.include_router(dmo_frame_controller.router)
app.include_router(dmo_galvanized_controller.router)
app.include_router(dmo_board_controller.router)
app.include_router(dmo_railing_controller.router)
app.include_router(dmo_finishing_controller.router)
app.include_router(dmo_rain_scape_controller.router)


if __name__ == "__main__":
    uvicorn.run(app="app.main:app", host="0.0.0.0", port=8000, reload=True)
