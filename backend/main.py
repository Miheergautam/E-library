from fastapi import FastAPI, HTTPException
from database import books_collection
from models import Book
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# cors
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    try:
        await books_collection.database.command("ping")
        return {"message": "MongoDB Connected!"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/books")
async def get_books():
    books = await books_collection.find().to_list(100)
    return [
        {"id": str(book["_id"]), "title": book["title"], "author": book["author"], "description": book["description"], "pdf_url": book["pdf_url"]}
        for book in books
    ]

@app.get("/books/{book_id}")
async def get_book(book_id: str):
    book = await books_collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return {"id": str(book["_id"]), "title": book["title"], "author": book["author"], "description": book["description"], "pdf_url": book["pdf_url"]}
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
async def create_book(book: Book):
    new_book = await books_collection.insert_one(book.model_dump())
    return {"id": str(new_book.inserted_id), **book.model_dump()}

@app.put("/books/{book_id}")
async def update_book(book_id: str, book: Book):
    updated_book = await books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": book.model_dump()})
    if updated_book.modified_count:
        return {"message": "Book updated successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: str):
    deleted_book = await books_collection.delete_one({"_id": ObjectId(book_id)})
    if deleted_book.deleted_count:
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")