# E-Library Backend

## Overview
The E-Library Backend is built using FastAPI and connects to MongoDB Atlas for storing book information. It exposes RESTful API endpoints for managing books, including adding, updating, deleting, and retrieving book details. The backend allows book content retrieval via URLs for PDF viewing.

---

## Features
- **CRUD operations** for books (Create, Read, Update, Delete).
- **MongoDB Atlas** integration.
- **Secure MongoDB connection** using SSL.
- **Search functionality** for books.
- **Book content retrieval** via PDF URLs.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Miheergautam/e-library-backend.git
cd e-library-backend
```

### 2. Set Up Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file and add your MongoDB URI:
```plaintext
MONGO_URI=mongodb+srv://your-username:your-password@cluster0.mongodb.net/elibrary?retryWrites=true&w=majority
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```
The server will run at `http://127.0.0.1:8000`.

---

## Endpoints

### 1. Ping Database
```http
GET /ping
```

### 2. Get All Books
```http
GET /books
```

### 3. Get Book by ID
```http
GET /books/{book_id}
```

### 4. Add a New Book
```http
POST /books
```
#### Request Body:
```json
{
  "title": "...",
  "author": "....",
  "description": "....",
  "pdf_url": "..."
}
```

### 5. Update a Book
```http
PUT /books/{book_id}
```
#### Request Body:
```json
{
  "title": "...",
  "author": "...",
  "description": "...",
  "pdf_url": "..."
}
```

### 6. Delete a Book
```http
DELETE /books/{book_id}
```

---

## Project Structure
```
e-library-backend/
├── main.py            # FastAPI application
├── database.py        # MongoDB connection setup
├── models.py          # Pydantic models for books
├── schemas.py         # Input/output validation
├── .env               # MongoDB URI and other environment variables
├── .gitignore         # Git ignore file
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Dependencies
- **FastAPI** - Modern web framework for APIs.
- **Uvicorn** - ASGI server for FastAPI.
- **Motor** - Async MongoDB driver.
- **Pydantic** - Data validation.
- **python-dotenv** - Environment variable management.
- **certifi** - SSL certificate validation.

---

## Contributing
Feel free to fork this project and submit pull requests. For bugs or feature requests, open an issue.

---

## License
This project is licensed under the MIT License.