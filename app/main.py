# ToDo
# [/] venv within docker
# [X] motor_asyncio for async requests to database.
#    -> Maybe not.
# [X] ObjectId
#    -> Using UUID for id field.
# [ ] criar paginação nos métodos read_all ($skip e $limit)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (customer, material, quote, deck_quote, deck_board_template)

app = FastAPI()

origins = [
    "http://localhost:4201",
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
    return {"message": "Hello World"}


app.include_router(customer.router)
app.include_router(material.router)
app.include_router(deck_quote.router)
app.include_router(deck_board_template.router)
app.include_router(quote.router)


if __name__ == "__main__":
    uvicorn.run(app='app.main:app', host="0.0.0.0", port=8000, reload=True)
