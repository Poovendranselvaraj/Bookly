from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app= FastAPI()

books=[
    {"id":1,
     "title":"Think Python",
     "author":"Allen B. Downey",
     "publisher":"O'Reilly Media",
     "pulished_date":"2015-11-22",
     "page_count":1234,
     "language":"English",
    },
    {
    "id":2,
     "title":"Django y Example",
     "author":"Antonio Molina",
     "publisher":"Packt Published ltd",
     "pulished_date":"2022-11-12",
     "page_count":1250,
     "language":"English",
    },
    {
    "id":3,
     "title":"The web socket handbook",
     "author":"Alex Diaconu",
     "publisher":"Xinyu Wang",
     "pulished_date":"2012-01-01",
     "page_count":1034,
     "language":"English",
    },
    {
    "id":4,
     "title":"Head first JavaScript",
     "author":"Hellen Smith",
     "publisher":"Oreilly Media",
     "pulished_date":"2021-01-01",
     "page_count":234,
     "language":"English",
    },
    {
    "id":5,
     "title":"Algorithms and Data Structure in Python",
     "author":"Kent Lee",
     "publisher":"Springer .Inc",
     "pulished_date":"2022-01-01",
     "page_count":9034,
     "language":"English",
    },
    {
    "id":6,
     "title":"Head First HTML5 Programming",
     "author":"Eric T Freeman",
     "publisher":"O'Reilly Media",
     "pulished_date":"2011-21-01",
     "page_count":3001,
     "language":"English",
    },
    
]

class Book(BaseModel):
     id:int
     title:str
     author:str
     publisher:str
     pulished_date:str
     page_count:int
     language:str
@app.get('/books',response_model=List[Book])
async def get_all_books():  
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book)-> dict:
    new_book=book_data.model_dump()

    books.append(new_book)

    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id:int)-> dict:
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(
        Status_code=status.HTTP_404_NOT_FOUND,
        detail="book not found"
        )
@app.put('/books/{book_id}')
async def update_book(book_id:int)-> dict:
    pass

@app.delete('/books/{book_id}') 
async def delete_book(book_id:int)-> dict:
    pass