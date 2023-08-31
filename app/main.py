# ToDo
# [/] venv within docker
# [X] motor_asyncio for async requests to database.
#    -> Maybe not.
# [X] ObjectId
#    -> Letting MongoDB create document ids, and tranforming them into strings when reading from DB.
# [ ] criar paginação nos métodos read_all ($skip e $limit)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import (customer, decking_board_catalog, decking_quote,
                           decking_railing_catalog, material, quote)

app = FastAPI()

origins = [
    "http://localhost:4201",
    "http://localhost:4200",
    "https://wquote.onrender.com"
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


app.include_router(customer.router)
app.include_router(material.router)
app.include_router(quote.router)

app.include_router(decking_quote.router)
app.include_router(decking_board_catalog.router)
app.include_router(decking_railing_catalog.router)


if __name__ == "__main__":
    uvicorn.run(app='app.main:app', host="0.0.0.0", port=8000, reload=True)
